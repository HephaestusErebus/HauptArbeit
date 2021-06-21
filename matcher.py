import common
import math

dist_lim = 120
sqr_dist_lim = common.sqr(dist_lim)

d_dist_lim_coef = 0.05

ang_upp_lim = 348
ang_dwn_lim = 12

edgs_dist = 0
edgs_bet1 = 1
edgs_bet2 = 2

def angle_delta_accepted(bet_prb, bet_gal):
    d_bet = abs(bet_prb - bet_gal)
    return d_bet < ang_dwn_lim or d_bet > ang_upp_lim


def angleFromRads(rads):
    theta = rads * 180 / math.pi
    theta = common.angle_in_range(theta)
    return theta

class matcher():

    def __init__(self):
        self.prb_edgs = [] # table of relatively close minutiae pairs in probe fingerprint ordered by distance
        self.gal_edgs = [] # table of relatively close minutiae pairs in gallery fingerprint ordered by distance
        self.cmp_edgs = [] # table of compatible edges pairs from probe and gallery edges ordered by probe edge id
        self.lngst_path = []  # biggest founded subset of cmp_edgs

    def comp_rel_meas(self, mnt_set:list):
        edg_table = []
        mnt_count = len(mnt_set)

        # mnt_set has to be sorted by X position increased
        # make pairwise comparison for each relatively close minutiae

        for i in range(mnt_count-1):
            for j in range(i+1, mnt_count):
                # check if vectors collinear and theta(i) == theta(j) + n*pi needed?

                # calculate delta x and delta y between i and j minutiaes positions
                dx = mnt_set[j][common.x_col_id] - mnt_set[i][common.x_col_id]
                dy = mnt_set[j][common.y_col_id] - mnt_set[i][common.y_col_id]
                # find distance between them
                sqr_dist = common.sqr(dx) + common.sqr(dy)

                # if j mnt is too far from i mnt, we'll not count it
                # if dx greater then dist_limit, then drop computations for i-th mnt
                # since mnt_set is sorted by X position
                if (sqr_dist > sqr_dist_lim):
                    if dx > dist_lim:
                        break
                    else:
                        continue

                # calculate angle of intervening line between minutiaes
                theta_ij = math.degrees(math.atan(dy/dx)) if dx > 0 else 90
                theta_ij += 0.5 if theta_ij > 0 else -0.5
                theta_ij = int(theta_ij)

                # calculate angle between i(j) minutiae orientation and intervening line
                # in range [-pi; pi]
                beta_1 = common.angle_in_range(theta_ij - mnt_set[i][common.t_col_id])
                beta_2 = common.angle_in_range(theta_ij - mnt_set[j][common.t_col_id])

                print(mnt_set[i][common.t_col_id], mnt_set[j][common.t_col_id], beta_1,  beta_2)
                # beta_1 = min(beta_i, beta_j); beta_2 = max(beta_i, beta_j)
                if beta_1 > beta_2:
                    beta_1, beta_2 = beta_2, beta_1
                # current edge data for edges table
                cur_edg = [sqr_dist, beta_1, beta_2, i, j, theta_ij]

                # find id of first edge in table with distance > current_edge_distance
                nr_dist_edg = len(edg_table)
                for edg in range(len(edg_table)):
                    if edg_table[edg][edgs_dist] > sqr_dist:
                        nr_dist_edg = edg
                        break

                # if no edges with distance greater then current_edge_distance found
                # insert at the end of edges table. Otherwise, insert at founded id
                if nr_dist_edg != len(edg_table):
                    edg_table.insert(nr_dist_edg, cur_edg)
                else:
                    edg_table.append(cur_edg)

        return edg_table

    def find_cmpt_edgs(self, prb_edgs, gal_edgs):
        # get count of probe and gallery fingerprint edges
        prb_edgs_count = len(prb_edgs)
        gal_edgs_count = len(gal_edgs)

        # id of the last incompatible edge in gal_edges for which following condition is true:
        # prb_edgs[p_edg][edg_dist] - gal_edgs[farest_edg][edg_dist] > d_dist_lim
        # since all rows in prb_edgs sorted by distance, this condition will be correct
        # for any n_p >= p_edg and any n_g <= farest_edg
        farest_edg = -1

        # for each probe edge find compatible gallery edge. To limit useless calculations
        # search in gallery_edges goes from farest_edg to first edge for which following
        # condition is true: prb_edgs[p_edg][edg_dist] - gal_edgs[g_edg][edg_dist] < -d_dist_lim
        cur_lowest_delta, cur_gal_edg = 9999, -1
        selected_gal_edgs = set()
        for p_edg in range(prb_edgs_count):
            for g_edg in range(farest_edg+1, gal_edgs_count):
                if g_edg in selected_gal_edgs:
                    continue
                # calculate delta distance and delta distance limit for current pair of edges
                d_dist = prb_edgs[p_edg][edgs_dist] - gal_edgs[g_edg][edgs_dist]
                d_dist_lim = (prb_edgs[p_edg][edgs_dist] + gal_edgs[g_edg][edgs_dist]) * (d_dist_lim_coef/2)

                # if delta_distance greater then delta distance limit, skip this pair
                if abs(d_dist) >= d_dist_lim:
                    # if delta distance is positive, then check if this is the farest edge
                    if d_dist > 0:
                        farest_edg = max(g_edg, farest_edg)
                        continue
                    # if delta distance is negative, stop calculations for this probe_edg
                    else:
                        break
                # get beta_1 and beta_2 values for gallery and  probe fingerprints
                prb_bet1, prb_bet2 = prb_edgs[p_edg][edgs_bet1], prb_edgs[p_edg][edgs_bet2]
                gal_bet1, gal_bet2 = gal_edgs[g_edg][edgs_bet1], gal_edgs[g_edg][edgs_bet2]

                # check if delta beta_1 and delta beta_2 in acceptable range
                # skip this pair otherwise
                if not (angle_delta_accepted(prb_bet1, gal_bet1) and angle_delta_accepted(prb_bet2, gal_bet2)):
                    continue

                # find delta value for all 3 measures
                delta = abs(int(prb_bet1-gal_bet1))%ang_upp_lim + abs(int(prb_bet2-gal_bet2))%ang_upp_lim + abs(d_dist)

                if delta < cur_lowest_delta:
                    cur_lowest_delta, cur_gal_edg = delta, g_edg

            if cur_gal_edg >= 0:
                selected_gal_edgs.add(cur_gal_edg)
                cur_lowest_delta, cur_gal_edg = 9999, -1

        return len(selected_gal_edgs)

    def init_probe_fingerprint(self, mnt_set: list):
        self.prb_edgs = self.comp_rel_meas(mnt_set)

    def init_gallery_fingerprint(self, mnt_set: list):
        self.gal_edgs = self.comp_rel_meas(mnt_set)

    def get_match_score(self):
        score = self.find_cmpt_edgs(self.prb_edgs, self.gal_edgs)
        return score