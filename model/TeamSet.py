from model import Team as T
from data import Const as C
import math

"""
Defines a set of two teams, with all 10 players
"""


class TeamSet:
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):

        self.t1 = T.Team(p1, p2, p3, p4, p5)
        self.t2 = T.Team(p6, p7, p8, p9, p10)

        self.score = 0
        self.rating = 0
        self.level_diff = 0
        self.role_pref = 0
        self.value_diff = 0
        self.synergy = 0
        self.calc_score()

    def __hash__(self):
        return hash(self.t1) + hash(self.t2)

    def __eq__(self, other):
        return (self.t1 == other.t1 and self.t2 == other.t2) or (self.t1 == other.t2 and self.t2 == other.t1)

    def __ne__(self, other):
        return not self.__eq__(other)

    # Calculate a team score ranging from 0 to 1.
    def calc_score(self):

        avg_rating = (self.t1.rank_sum + self.t2.rank_sum) / 10 / C.AVG_RANK

        # Scale such that 0 diff = 1.
        level_diff = math.exp(-abs(self.t1.rank_sum - self.t2.rank_sum)/5)  # Avg diff in rank per player

        pref_role_sum = (self.t1.role_pref + self.t2.role_pref) / C.MAX_ROLE_PREF  # 1 if everyone on their fav role(s)

        synergy = (self.t1.synergy_sum + self.t2.synergy_sum) / 10 + 1  # Total synergy score per player + 1
        value_diff = math.exp(- abs(self.t1.value - self.t2.value))

        self.rating = round(avg_rating, 2)
        self.level_diff = round(level_diff, 2)
        self.role_pref = round(pref_role_sum, 2)
        self.synergy = round(synergy, 2)
        self.value_diff = round(value_diff, 2)

        # Give each team a score out of 1 by using the given weights for the three categories.
        score = avg_rating * C.weight_factors[0] + \
            pref_role_sum * C.weight_factors[1] + \
            level_diff * C.weight_factors[2] + \
            synergy * C.weight_factors[3] + \
            value_diff * C.weight_factors[4]

        score = round(score, 5)  # 5 Decimal places
        self.score = score

    def detailed_score(self):
        return "Score Parameters (Each field is out of 1)\n" +\
        "Role Pref = " + str(self.role_pref) + "\n" + \
        "Level Diff = " + str(self.level_diff) + "\t" + \
            str(self.t1.rank_sum) + " vs " + str(self.t2.rank_sum) + "\n" + \
        "Synergy Score = " + str(self.synergy) + "\n" + \
        "Rating = " + str(self.rating) + "\n" + \
        "Value Diff = " + str(self.value_diff) + "\t" + str(self.t1.value) + " vs " + str(self.t2.value) + "\n" + \
            "\tComms " + str(self.t1.comms_value) + " vs " + str(self.t2.comms_value) + "\n" + \
            "\tFlex " + str(self.t1.flex_value) + " vs " + str(self.t2.flex_value) + "\n" + \
            "\tUntilt" + str(self.t1.untilt_value) + " vs " + str(self.t2.untilt_value) + "\n" + \
            "\tConsistency" + str(self.t1.consist_value) + " vs " + str(self.t2.consist_value)

    def to_string(self):
        return self.t1.players[0].name + "\t\t" + self.t2.players[0].name + "\n" + \
            self.t1.players[1].name + "\t\t" + self.t2.players[1].name + "\n" + \
            self.t1.players[2].name + "\t\t" + self.t2.players[2].name + "\n" + \
            self.t1.players[3].name + "\t\t" + self.t2.players[3].name + "\n" + \
            self.t1.players[4].name + "\t\t" + self.t2.players[4].name

