from data import Role as R
from data import Const as C

'''
Defines a team with 5 players
'''


class Team:
    def __init__(self, p1, p2, p3, p4, p5):
        self.players = [p1, p2, p3, p4, p5]

        level = 0
        role_pref = 0
        for i in range(0, len(self.players)):
            level += self.players[i].rating[i]
            role_pref += self.players[i].rolePref[i]

        self.rank_sum = level
        self.level = level / 5 / R.LPl

        comms_value = 0
        flex_value = 0
        untilt_value = 0
        consist_value = 0
        value = 0
        corr_sum = 0
        for p in self.players:
            value += p.value
            comms_value += p.comms_value
            flex_value += p.flex_value
            untilt_value += p.untilt_value
            consist_value += p.consist_value

            for cor in C.corr_map[p.name]:
                if cor.player in self.players:
                    corr_sum += cor.score

        self.comms_value = round(comms_value, 2)
        self.flex_value = round(flex_value, 2)
        self.untilt_value = round(untilt_value, 2)
        self.consist_value = round(consist_value, 2)
        self.value = round(value, 4)
        self.other_values = [comms_value, flex_value, untilt_value, consist_value]

        self.role_pref = role_pref
        self.synergy_sum = corr_sum
        self.synergy = corr_sum / 10 + 1

        score = self.level * C.weight_factors[0] + \
            self.role_pref * C.weight_factors[1] + \
            self.synergy * C.weight_factors[3] + \
            self.value * C.weight_factors[4]

        self.score = round(score, 5)  # 5 Decimal places

    def __hash__(self):
        return hash(self.players[0]) * 5 + hash(self.players[1]) * 4 + hash(self.players[2]) * 3 + hash(self.players[3]) * 2 + hash(self.players[4])

    def __eq__(self, other):
        return self.players[0] == other.players[0] and \
            self.players[1] == other.players[1] and \
            self.players[2] == other.players[2] and \
            self.players[3] == other.players[3] and \
            self.players[4] == other.players[4]

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_string(self):
        return self.players[0].name + " " + self.players[1].name + " " + self.players[2].name + " " + \
               self.players[3].name + " " + self.players[4].name + "\nScore " + str(self.score)

    def detailed_score(self):
        return ""
