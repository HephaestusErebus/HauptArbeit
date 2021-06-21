import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QColor, QPainter, QPen
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from mainwindow import Ui_MainWindow
from MinutiaeNet.NeuralNetwork import NeuralNetwork
from matcher import matcher

import common
from database import DatabaseController
from dialog_windows import addUserDialog, selectPersonDialog, showResultDialog

def isPixelZero(colorValue):
    c = QColor(colorValue).getRgb()
    return c[0] == 0 and c[1] == 0 and c[2] == 0

def angleFromRads(rads):
    theta = rads * 180 / math.pi
    theta = common.angle_in_range(theta)
    return theta

detectionThreshold = 125
robustDetectionThreshold = 300

MinutiaeNet: NeuralNetwork = None
passedFilterTemplate = 'Total amount of {} minutiaes met the criteria'

def swapImageColors(origImg: QImage):
    for x in range(origImg.width()):
        for y in range(origImg.height()):
            c = origImg.pixel(x, y)
            if isPixelZero(c):
                origImg.setPixel(x, y, 0)
            else:
                origImg.setPixel(x, y, 1)
    return origImg


def blackWhiteMask(origImg: QImage):
    for x in range(1, origImg.width()-1, 2):
        for y in range(1, origImg.height()-1, 2):
            c1, c2 = origImg.pixel(x-1, y-1), origImg.pixel(x-1, y)
            c3, c4 = origImg.pixel(x, y-1), origImg.pixel(x, y)
            mask = isPixelZero(c1) + isPixelZero(c2) + isPixelZero(c3) + isPixelZero(c4)
            if mask <= 2:
                origImg.setPixel(x-1, y-1, 0)
                origImg.setPixel(x-1, y, 0)
                origImg.setPixel(x, y-1, 0)
                origImg.setPixel(x, y, 0)
            else:
                origImg.setPixel(x - 1, y - 1, 1)
                origImg.setPixel(x - 1, y, 1)
                origImg.setPixel(x, y - 1, 1)
                origImg.setPixel(x, y, 1)
    return origImg

def drawMinutiae(painter:QPainter, mnt, scaleX, scaleY):
    scaledX, scaledY = mnt[0] * scaleX, mnt[1] * scaleY
    painter.drawEllipse(scaledX-6, scaledY-6, 12, 12)
    rotatedX = 10 * math.cos(mnt[2] * math.pi / 180) + scaledX
    rotatedY = 10 * math.sin(mnt[2] * math.pi / 180) + scaledY
    painter.drawLine(scaledX, scaledY, rotatedX, rotatedY)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.originalFingerprint_lbl.setScaledContents(True)
        self.procceedFingerprint_lbl.setScaledContents(True)
        self.connectSlots()

        self.dbController = DatabaseController()
        self.addPersonForm = addUserDialog(self.dbController)
        self.selectPersonForm = selectPersonDialog(self.dbController)
        self.matchResultForm = showResultDialog()
        self.fingerMatcher = matcher()

        self.curFingerImg: QImage = None
        self.clrSwappedPxm: QPixmap = None
        self.maskedPxm: QPixmap = None
        self.proceedPxm: QPixmap = None

        self.mntsList: list = None
        self.fltrdMnts: list = None
        self.curMntId = 0

    def connectSlots(self):
        self.loadImage_pB.clicked.connect(self.loadFingerImg)
        self.procceedImage_pB.clicked.connect(self.proceedFingerImg)
        self.fingerprintMinutiaes_lst.currentItemChanged.connect(self.markCurrentMnt)
        self.findMatch_pB.clicked.connect(self.findBestMatch)
        self.addPerson_pB.clicked.connect(self.showAddPersonForm)
        self.saveInDb_pB.clicked.connect(self.showSelectPersonForm)
        self.accuracyThresValue_sB.valueChanged.connect(self.updFilterMnts)


    def loadFingerImg(self):
        imgName = QFileDialog.getOpenFileName(self, 'Open fingerprint Image', '',
                                              'Image files (*.jpg *.png *.bmp *.tif)')
        self.curFingerImg = QImage(str(imgName[0]))
        self.curFingerImg.save('current.bmp')

        clrSwappedFingerImg = self.curFingerImg.copy()
        clrSwappedFingerImg = clrSwappedFingerImg.convertToFormat(QImage.Format_Mono)
        clrSwappedFingerImg = swapImageColors(clrSwappedFingerImg)

        self.clrSwappedPxm = QPixmap(clrSwappedFingerImg)
        self.clrSwappedPxm = self.clrSwappedPxm.scaled(self.originalFingerprint_lbl.width(),
                                                             self.originalFingerprint_lbl.height(),
                                                             Qt.IgnoreAspectRatio)

        maskedFingerImg = blackWhiteMask(clrSwappedFingerImg)
        self.maskedPxm = QPixmap(maskedFingerImg)
        self.maskedPxm = self.maskedPxm.scaled(self.originalFingerprint_lbl.width(),
                                                             self.originalFingerprint_lbl.height(),
                                                             Qt.IgnoreAspectRatio)
        self.originalFingerprint_lbl.setPixmap(self.clrSwappedPxm)


    def proceedFingerImg(self):
        self.mntsList = MinutiaeNet.getMinutiaePoints().tolist()
        self.mntsList.sort(key=lambda x: x[common.q_col_id])
        self.mntsList = self.mntsList[:200]
        for mnt in self.mntsList:
            mnt[common.t_col_id] = angleFromRads(mnt[2])
            mnt[common.x_col_id], mnt[common.y_col_id] = int(mnt[common.x_col_id]), int(mnt[common.y_col_id])
            mnt[common.q_col_id] *= 100

        self.mntsList.sort(key=lambda x: x[common.x_col_id])
        self.updFilterMnts()

    def updFilterMnts(self):
        self.fltrdMnts = [mnt for mnt in self.mntsList if mnt[common.q_col_id] > self.accuracyThresValue_sB.value()]
        self.fingerprintMinutiaes_lst.clear()
        for mnt in self.fltrdMnts:
            mntCaption = str('  X=' + str(mnt[common.x_col_id]) + ';').ljust(11) + 'Y=' + str(mnt[common.y_col_id])
            self.fingerprintMinutiaes_lst.addItem(mntCaption)

        self.mntAmount_lbl.setText(passedFilterTemplate.format(len(self.fltrdMnts)))
        self.curMntId = -1
        self.mntOreintationValue_lE.clear(), self.mntAccuracyValue_lE.clear()
        self.drawMinutiaes()

    def drawMinutiaes(self):
        self.proceedPxm = self.maskedPxm.copy()
        painter = QPainter(self.proceedPxm)

        scaleWidth = self.clrSwappedPxm.width() / self.curFingerImg.width()
        scaleHeight = self.clrSwappedPxm.height() / self.curFingerImg.height()

        pen = QPen(Qt.blue, 3)
        painter.setPen(pen)
        for mnt in self.fltrdMnts:
            drawMinutiae(painter, mnt, scaleWidth, scaleHeight)

        self.procceedFingerprint_lbl.setPixmap(self.proceedPxm)

    def markCurrentMnt(self):
        if self.curMntId >= len(self.fltrdMnts):
            return

        painter = QPainter(self.proceedPxm)

        scaleWidth = self.proceedPxm.width() / self.curFingerImg.width()
        scaleHeight = self.proceedPxm.height() / self.curFingerImg.height()

        pen = QPen(Qt.blue, 3)
        painter.setPen(pen)
        if (self.curMntId >= 0):
            drawMinutiae(painter, self.fltrdMnts[self.curMntId], scaleWidth, scaleHeight)

        self.curMntId = self.fingerprintMinutiaes_lst.currentRow()
        pen = QPen(Qt.red, 3)
        painter.setPen(pen)
        drawMinutiae(painter, self.fltrdMnts[self.curMntId], scaleWidth, scaleHeight)
        self.procceedFingerprint_lbl.setPixmap(self.proceedPxm)

        self.mntAccuracyValue_lE.setText("{:100.1f}".format(self.fltrdMnts[self.curMntId][common.q_col_id]))
        self.mntOreintationValue_lE.setText(str(-self.fltrdMnts[self.curMntId][common.t_col_id]))

    def showAddPersonForm(self):
        self.addPersonForm.getPersonData()

    def showSelectPersonForm(self):
        if len(self.fltrdMnts):
            self.selectPersonForm.selectOwner(self.fltrdMnts)

    def findBestMatch(self):
        searchStep, procCount = 100, 0
        scores, robustMatchFound = {}, False
        self.fingerMatcher.init_probe_fingerprint(self.fltrdMnts)
        while True:
            fingerprints = self.dbController.getFingerprints(procCount, searchStep)
            procCount += searchStep
            for fprint in fingerprints:
                self.fingerMatcher.init_gallery_fingerprint(fprint.mntsList)
                score = self.fingerMatcher.get_match_score()
                if fprint.ownerId in scores:
                    if score > scores[fprint.ownerId]:
                        scores[fprint.ownerId] = score
                else:
                    scores[fprint.ownerId] = score

                if score > robustDetectionThreshold:
                    robustMatchFound = True
                    break

            if len(fingerprints) < searchStep or robustMatchFound:
                break

        matchRes = 'No match found'
        if len(scores) > 0:
            bestMatchId = max(scores, key=scores.get())
            if scores[bestMatchId] > detectionThreshold:
                matchRes = '{0} with score {1}'.format(self.dbController.getPersonName(bestMatchId), scores[bestMatchId])

        self.matchResultForm.showMatchResult(matchRes)


if __name__ == '__main__':
    MinutiaeNet = NeuralNetwork()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())