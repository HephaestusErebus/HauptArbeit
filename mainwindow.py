# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(920, 530))
        MainWindow.setMaximumSize(QtCore.QSize(920, 530))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(920, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 901, 501))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.origImage_gB = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.origImage_gB.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.origImage_gB.setFont(font)
        self.origImage_gB.setAutoFillBackground(False)
        self.origImage_gB.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(0,0,0);\n"
"    color: rgb(255,255,255);\n"
"}")
        self.origImage_gB.setObjectName("origImage_gB")
        self.loadImage_pB = QtWidgets.QPushButton(self.origImage_gB)
        self.loadImage_pB.setGeometry(QtCore.QRect(70, 377, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.loadImage_pB.setFont(font)
        self.loadImage_pB.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.loadImage_pB.setObjectName("loadImage_pB")
        self.procceedImage_pB = QtWidgets.QPushButton(self.origImage_gB)
        self.procceedImage_pB.setGeometry(QtCore.QRect(70, 420, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.procceedImage_pB.setFont(font)
        self.procceedImage_pB.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.procceedImage_pB.setObjectName("procceedImage_pB")
        self.originalFingerprint_lbl = QtWidgets.QLabel(self.origImage_gB)
        self.originalFingerprint_lbl.setGeometry(QtCore.QRect(15, 30, 250, 320))
        self.originalFingerprint_lbl.setStyleSheet("QLabel{\n"
"    background-color: rgb(75, 75, 75);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: gray;\n"
"}\n"
"")
        self.originalFingerprint_lbl.setText("")
        self.originalFingerprint_lbl.setObjectName("originalFingerprint_lbl")
        self.horizontalLayout.addWidget(self.origImage_gB)
        self.procceeImage_gB = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.procceeImage_gB.setMinimumSize(QtCore.QSize(0, 0))
        self.procceeImage_gB.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.procceeImage_gB.setFont(font)
        self.procceeImage_gB.setAutoFillBackground(False)
        self.procceeImage_gB.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(0,0,0);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"     background: black;;\n"
"     width: 17px;    \n"
"     margin: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    background: rgb(170, 0, 0);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"    margin: 2px;\n"
"    margin-left: 4px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"\n"
"    background: red;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical \n"
"{\n"
"     background: none;\n"
" }\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    background: none;\n"
" }\n"
" \n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical \n"
"{\n"
"    background: none;\n"
" }\n"
"")
        self.procceeImage_gB.setObjectName("procceeImage_gB")
        self.fingerprintMinutiaes_lst = QtWidgets.QListWidget(self.procceeImage_gB)
        self.fingerprintMinutiaes_lst.setGeometry(QtCore.QRect(340, 40, 211, 291))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.fingerprintMinutiaes_lst.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.fingerprintMinutiaes_lst.setFont(font)
        self.fingerprintMinutiaes_lst.setStyleSheet("QListWidget\n"
"{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.fingerprintMinutiaes_lst.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.fingerprintMinutiaes_lst.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fingerprintMinutiaes_lst.setObjectName("fingerprintMinutiaes_lst")
        self.fingerprintMinutiaes_lbl = QtWidgets.QLabel(self.procceeImage_gB)
        self.fingerprintMinutiaes_lbl.setGeometry(QtCore.QRect(350, 15, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.fingerprintMinutiaes_lbl.setFont(font)
        self.fingerprintMinutiaes_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.fingerprintMinutiaes_lbl.setObjectName("fingerprintMinutiaes_lbl")
        self.mntAmount_lbl = QtWidgets.QLabel(self.procceeImage_gB)
        self.mntAmount_lbl.setGeometry(QtCore.QRect(300, 345, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.mntAmount_lbl.setFont(font)
        self.mntAmount_lbl.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.mntAmount_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.mntAmount_lbl.setWordWrap(True)
        self.mntAmount_lbl.setObjectName("mntAmount_lbl")
        self.accuracyThresValue_sB = QtWidgets.QSpinBox(self.procceeImage_gB)
        self.accuracyThresValue_sB.setGeometry(QtCore.QRect(500, 393, 50, 24))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.accuracyThresValue_sB.setFont(font)
        self.accuracyThresValue_sB.setStyleSheet("QSpinBox{\n"
"    background-color: rgb(75, 75, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSpinBox::up-button { \n"
"    border-down: 2px solid rgb(75, 75, 75);\n"
"    background-color: rgb(170, 0, 0);\n"
"    text:\'^\'\n"
"}\n"
"\n"
"QSpinBox::down-button { \n"
"    \n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.accuracyThresValue_sB.setFrame(True)
        self.accuracyThresValue_sB.setMinimum(50)
        self.accuracyThresValue_sB.setDisplayIntegerBase(10)
        self.accuracyThresValue_sB.setObjectName("accuracyThresValue_sB")
        self.groupBox = QtWidgets.QGroupBox(self.procceeImage_gB)
        self.groupBox.setGeometry(QtCore.QRect(10, 370, 261, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.mntOreintationValue_lE = QtWidgets.QLineEdit(self.groupBox)
        self.mntOreintationValue_lE.setGeometry(QtCore.QRect(195, 15, 45, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.mntOreintationValue_lE.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.mntOreintationValue_lE.setFont(font)
        self.mntOreintationValue_lE.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.mntOreintationValue_lE.setReadOnly(True)
        self.mntOreintationValue_lE.setObjectName("mntOreintationValue_lE")
        self.percentSymbol_lbl = QtWidgets.QLabel(self.groupBox)
        self.percentSymbol_lbl.setGeometry(QtCore.QRect(245, 50, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.percentSymbol_lbl.setFont(font)
        self.percentSymbol_lbl.setStyleSheet("QLabel\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.percentSymbol_lbl.setObjectName("percentSymbol_lbl")
        self.mntAccuracy_lbl = QtWidgets.QLabel(self.groupBox)
        self.mntAccuracy_lbl.setGeometry(QtCore.QRect(32, 50, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.mntAccuracy_lbl.setFont(font)
        self.mntAccuracy_lbl.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.mntAccuracy_lbl.setObjectName("mntAccuracy_lbl")
        self.mntOrientation_lbl = QtWidgets.QLabel(self.groupBox)
        self.mntOrientation_lbl.setGeometry(QtCore.QRect(5, 15, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.mntOrientation_lbl.setFont(font)
        self.mntOrientation_lbl.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.mntOrientation_lbl.setObjectName("mntOrientation_lbl")
        self.mntAccuracyValue_lE = QtWidgets.QLineEdit(self.groupBox)
        self.mntAccuracyValue_lE.setGeometry(QtCore.QRect(195, 50, 45, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.mntAccuracyValue_lE.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.mntAccuracyValue_lE.setFont(font)
        self.mntAccuracyValue_lE.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.mntAccuracyValue_lE.setReadOnly(True)
        self.mntAccuracyValue_lE.setObjectName("mntAccuracyValue_lE")
        self.degreeSymbol_lbl = QtWidgets.QLabel(self.groupBox)
        self.degreeSymbol_lbl.setGeometry(QtCore.QRect(245, 15, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.degreeSymbol_lbl.setFont(font)
        self.degreeSymbol_lbl.setStyleSheet("QLabel\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.degreeSymbol_lbl.setObjectName("degreeSymbol_lbl")
        self.accuracyThres_lbl = QtWidgets.QLabel(self.procceeImage_gB)
        self.accuracyThres_lbl.setGeometry(QtCore.QRect(310, 395, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.accuracyThres_lbl.setFont(font)
        self.accuracyThres_lbl.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.accuracyThres_lbl.setObjectName("accuracyThres_lbl")
        self.addPerson_pB = QtWidgets.QPushButton(self.procceeImage_gB)
        self.addPerson_pB.setGeometry(QtCore.QRect(280, 430, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.addPerson_pB.setFont(font)
        self.addPerson_pB.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.addPerson_pB.setObjectName("addPerson_pB")
        self.findMatch_pB = QtWidgets.QPushButton(self.procceeImage_gB)
        self.findMatch_pB.setGeometry(QtCore.QRect(500, 430, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.findMatch_pB.setFont(font)
        self.findMatch_pB.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.findMatch_pB.setObjectName("findMatch_pB")
        self.saveInDb_pB = QtWidgets.QPushButton(self.procceeImage_gB)
        self.saveInDb_pB.setGeometry(QtCore.QRect(390, 430, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.saveInDb_pB.setFont(font)
        self.saveInDb_pB.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.saveInDb_pB.setObjectName("saveInDb_pB")
        self.procceedFingerprint_lbl = QtWidgets.QLabel(self.procceeImage_gB)
        self.procceedFingerprint_lbl.setGeometry(QtCore.QRect(15, 30, 250, 320))
        self.procceedFingerprint_lbl.setStyleSheet("QLabel{\n"
"    background-color: rgb(75, 75, 75);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: gray;\n"
"}\n"
"")
        self.procceedFingerprint_lbl.setText("")
        self.procceedFingerprint_lbl.setObjectName("procceedFingerprint_lbl")
        self.horizontalLayout.addWidget(self.procceeImage_gB)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.origImage_gB.setTitle(_translate("MainWindow", "Original Image"))
        self.loadImage_pB.setText(_translate("MainWindow", "Load Image"))
        self.procceedImage_pB.setText(_translate("MainWindow", "Procceed Image"))
        self.procceeImage_gB.setTitle(_translate("MainWindow", "Procceed Image"))
        self.fingerprintMinutiaes_lbl.setText(_translate("MainWindow", "Minutiae points"))
        self.mntAmount_lbl.setText(_translate("MainWindow", "Total amount of 0 minutiaes met the criteria"))
        self.percentSymbol_lbl.setText(_translate("MainWindow", "%"))
        self.mntAccuracy_lbl.setText(_translate("MainWindow", "Minutiae accuracy:"))
        self.mntOrientation_lbl.setText(_translate("MainWindow", "Minutiae orientation:"))
        self.degreeSymbol_lbl.setText(_translate("MainWindow", "°"))
        self.accuracyThres_lbl.setText(_translate("MainWindow", "Accuracy threshold:"))
        self.addPerson_pB.setText(_translate("MainWindow", "Add Person"))
        self.findMatch_pB.setText(_translate("MainWindow", "Find Match"))
        self.saveInDb_pB.setText(_translate("MainWindow", "Save in DB"))