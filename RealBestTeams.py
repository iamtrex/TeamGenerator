import Role as R
import itertools
import math
import time

'''Class Def Player - Represents a Player with name, preferred roles, and rating at each role.'''


class Player:

    def __init__(self, name, rolePref, rating):
        self.name = name
        self.rolePref = rolePref
        self.rating = rating
        self.overElo = sum(rating)/len(rating)
        self.flexibility = sum(rolePref)/len(rolePref)

        value = 0
        for i in range(0, 5):
            value += rolePref[i] * rating[i]

        self.value = value/sum(rolePref) # Get Proper Average


    def total(self):
        return self.flexibility


class Corr:
    def __init__(self, player, score):
        self.player = player
        self.score = score

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
            role_pref += players[i].rolePref[i]

        self.level = level / 5 / R.LPl

        value = 0
        corr_sum = 0
        for p in self.players:
            value += p.value
            for cor in corr_map[p.name]:
                if cor.player in self.players:
                    corr_sum += cor.score

        self.value = value
        self.role_pref = role_pref
        self.corr_effect = corr_sum / 10 + 1

        score = self.level * weight_factors[0] + \
                self.role_pref * weight_factors[1] + \
                self.corr_effect * weight_factors[3] + \
                self.value * weight_factors[4]

        self.score = round(score, 5)  # 5 Decimal places
    def to_string(self):
        return self.players[0].name + " " + self.players[1].name + " " + self.players[2].name + " " + \
               self.players[3].name + " " + self.players[4].name + "\nScore " + str(self.score)





'''
Defines a set of two teams, with all 10 players 
'''
class Set:
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8
        self.p9 = p9
        self.p10 = p10
        self.t1 = [p1, p2, p3, p4, p5]
        self.t2 = [p6, p7, p8, p9, p10]
        self.score = 0
        self.rating = 0
        self.level_diff = 0
        self.role_pref = 0
        self.value_diff = 0
        self.t1_level = 0
        self.t2_level = 0
        self.t1_value = 0
        self.t2_value = 0
        self.corr_effect = 0

        self.calc_score()

    # Calculate a team score ranging from 0 to 1.
    def calc_score(self):
        t1_level = self.p1.rating[0] + self.p2.rating[1] + self.p3.rating[2] + self.p4.rating[3] + self.p5.rating[4]
        t2_level = self.p6.rating[0] + self.p7.rating[1] + self.p8.rating[2] + self.p9.rating[3] + self.p10.rating[4]
        # Scale such that avg rank = Low Plat
        avg_rating = (t1_level + t2_level) / 10 / R.LPl

        # Scale such that 0 diff = 1.
        level_diff = math.exp(- abs(t1_level - t2_level))


        t1_role_pref = self.p1.rolePref[0] + self.p2.rolePref[1] + self.p3.rolePref[2] + self.p4.rolePref[3] + self.p5.rolePref[4]
        t2_role_pref = self.p6.rolePref[0] + self.p7.rolePref[1] + self.p8.rolePref[2] + self.p9.rolePref[3] + self.p10.rolePref[4]

        role_sum = (t1_role_pref + t2_role_pref) / 30  # Everyone on top rolee will result in 1.

        t1_value = 0
        t2_value = 0
        corr_sum = 0
        for p in self.t1:
            t1_value += p.value
            for cor in corr_map[p.name]:
                if cor.player in self.t1:
                    corr_sum += cor.score

        for p in self.t2:
            t2_value += p.value
            for cor in corr_map[p.name]:
                if cor.player in self.t2:
                    corr_sum += cor.score


        corr_effect = corr_sum / 10 + 1 # This score can go over 1.

        value_diff = math.exp(-abs(t1_value - t2_value))

        self.t1_level = t1_level
        self.t2_level = t2_level
        self.t1_value = t1_value
        self.t2_value = t2_value
        self.rating = round(avg_rating, 2)
        self.level_diff = round(level_diff, 2)
        self.role_pref = round(role_sum, 2)
        self.corr_effect = round(corr_effect, 2)
        self.value_diff = round(value_diff, 2)

        # Give each team a score out of 1 by using the given weights for the three categories.
        score = avg_rating * weight_factors[0] + \
                role_sum * weight_factors[1] + \
                level_diff * weight_factors[2] + \
                corr_effect * weight_factors[3] + \
                value_diff * weight_factors[4]

        score = round(score, 5)  # 5 Decimal places
        self.score = score

    def to_string(self):
        return self.p1.name + "\t\t" + self.p6.name + "\n" + \
               self.p2.name + "\t\t" + self.p7.name + "\n" + \
               self.p3.name + "\t\t" + self.p8.name + "\n" + \
               self.p4.name + "\t\t" + self.p9.name + "\n" + \
               self.p5.name + "\t\t" + self.p10.name + "\n" + \
               "Role Pref = " + str(self.role_pref) + "\n" +\
               "Level Diff = " + str(self.level_diff) + "\t" + str(self.t1_level) + " vs " + str(self.t2_level) + "\n" +\
               "Corr Diff = " + str(self.corr_effect) + "\n" +\
               "Rating = " + str(self.rating) + "\n" +\
               "Value Diff = " + str(self.value_diff) + "\t" + str(self.t1_value) + " vs " + str(self.t2_value) + "\n"

def get_value(player):
    return player.value


def get_score(set):
    return set.score


def get_team_score(team):
    return team.score
'''
Begin Program!
'''
# Config Constants

keep_top_n = 3  # Keeps top n teams...
# 0.6, 0.3, 0.1 # Old weights
# Weights for the 3 factors : overall rank, pref roles, level diff, correlatabilities bonus, player stats
weight_factors = [0.50, 0.0, 0.30, 0.1, 0.1]
og = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Track Time execution
time_start = time.time()

# Setup all the players

# Setup Initial
'''
Andrew = Player("Andrew", [1, 3, 4, 2, 5], [R.LGo, R.MGo, R.LPl, R.MGo, R.LPl])
Rex = Player("Rex", [1, 5, 4, 3, 2],[R.LGo, R.HPl, R.HGo, R.LPl, R.HGo])
Fred = Player("Fred", [2, 1, 5, 3, 4],[R.MSi, R.LSi, R.HGo, R.MSi, R.LGo])
Justin = Player("Justin", [1, 3, 2, 5, 4], [R.LSi, R.HGo, R.MGo, R.LPl, R.HGo])
Josh = Player("Josh", [1, 2, 3, 5, 4], [R.MGo, R.MGo, R.HGo, R.MPl, R.LPl])
Jackie = Player("Jackie", [3, 5, 4, 1, 2], [R.MGo, R.MGo, R.MGo, R.LGo, R.LGo])
Charles = Player("Charles", [5, 1, 2, 4, 3], [R.LPl, R.HSi, R.MGo, R.MGo, R.MGo])
Jason = Player("Jason", [1, 5, 3, 2, 4], [R.HSi, R.HGo, R.MGo, R.HSi, R.MGo])
Victor = Player("Victor", [4, 1, 5, 3, 2], [R.HSi, R.LSi, R.LGo, R.HSi, R.HSi])
Tyson = Player("Tyson", [2, 1, 4, 3, 5], [R.LSi, R.LSi, R.HSi, R.HSi, R.MGo])
'''

# Setup New - Two Preferred Roles 1-3, with my rank adjustments... Rank from High Silver to M Plat
# Teamwork stuff - Comms, flexibility, untiltability
Andrew = Player("Andrew", [1, 2, 3, 2, 3], [R.LGo, R.MGo, R.LPl, R.MGo, R.LPl])
Rex = Player("Rex", [1, 3, 3, 3, 2],[R.LGo, R.MPl, R.HGo, R.LPl, R.HGo])
Fred = Player("Fred", [1, 1, 3, 2, 3],[R.HSi, R.HSi, R.HGo, R.LGo, R.MGo])
Justin = Player("Justin", [1, 2, 2, 3, 3], [R.LGo, R.HGo, R.LGo, R.LPl, R.HGo])
Josh = Player("Josh", [1, 2, 3, 3, 3], [R.MGo, R.MGo, R.HGo, R.MPl, R.LPl])
Jackie = Player("Jackie", [3, 3, 3, 1, 2], [R.HGo, R.HGo, R.MGo, R.LGo, R.LGo])
Charles = Player("Charles", [3, 1, 2, 2, 3], [R.HGo, R.HSi, R.LGo, R.MGo, R.MGo])
Jason = Player("Jason", [1, 3, 2, 2, 3], [R.HSi, R.HGo, R.LGo, R.HSi, R.LGo])
Victor = Player("Victor", [3, 1, 3, 3, 2], [R.LGo, R.HSi, R.MGo, R.MGo, R.HSi])
Tyson = Player("Tyson", [2, 1, 3, 1, 3], [R.LGo, R.HSi, R.LGo, R.HSi, R.MGo])

players = [Andrew, Rex, Fred, Justin, Josh, Jackie, Charles, Jason, Victor, Tyson]

corr_map = {
    "Andrew": {Corr(Jackie, -0.1), Corr(Justin, 0.5)},
    "Rex": {Corr(Jackie, -0.75), Corr(Andrew, 0.1)},
    "Fred": {Corr(Josh, 0.1), Corr(Rex, 0.1)},
    "Justin": {Corr(Tyson, -1.0)},
    "Josh": {Corr(Rex, -0.1)},
    "Jackie": {},
    "Charles": {Corr(Victor, 0.1), Corr(Tyson, 0.1)},
    "Jason": {Corr(Jackie, -0.2), Corr(Andrew, 0.1), Corr(Rex, 0.1)},
    "Victor": {Corr(Tyson, 0.5)},
    "Tyson": {}}

maxSets = []  # List of Sets, keeps top n

# Create all permutations

'''
allCombinations = itertools.permutations(og, 10)

counter = 0
scoreTotal = 0
for i in allCombinations:
    counter += 1
    if counter % 1000000 == 0:  # Print every million combinations
        print("Evaluated " + str(counter) + " combinations")
        if len(maxSets) > 0:
            print("Current Average " + str(scoreTotal/len(maxSets))) # Average over time... Should only improve

    # Create a set with the permutation.
    set = Set(players[i[0]], players[i[1]], players[i[2]], players[i[3]], players[i[4]],
              players[i[5]], players[i[6]], players[i[7]], players[i[8]], players[i[9]])

    score = get_score(set)

    if len(maxSets) < keep_top_n:
        maxSets.append(set)
        scoreTotal += score

    else:
        maxSets.sort(key=get_score, reverse=True)
        if get_score(maxSets[-1]) < score:
            # Pop Lowest score and replace with a new score...
            s = maxSets.pop()
            scoreTotal -= get_score(s)
            maxSets.append(set)
            scoreTotal += score

# Print Team from Best to Worst
i = 1
maxSets.sort(key=get_score, reverse=True)
for s in maxSets:
    print("Team Number " + str(i) + "\tScore: " + str(get_score(s)))
    print(s.to_string())
    i += 1
    print("\n")

# My Custom Team(s)
my_set = Set(Charles, Rex, Victor, Josh, Tyson, Jackie, Jason, Fred, Justin, Andrew)
print("My Team Score " + str(get_score(my_set)) + "\n" + my_set.to_string())
my_set_2 = Set(Charles, Jackie, Fred, Justin, Andrew, Victor, Jason, Rex, Josh, Tyson)
print("My Team Score " + str(get_score(my_set_2)) + "\n" + my_set_2.to_string())

print("Time Taken " + str(time.time() - time_start) + "s")


print("Player Abilities\n")

total_value = 0
for p in players:
    total_value += p.value

avg = round(total_value/len(players), 5)
players.sort(key=get_value)
for p in players:
    print(p.name + "\t" + str(round((p.value - avg)/avg, 3)))

'''


counter = 1
allCombinations = itertools.permutations(og, 5)
scoreTotal = 0
maxSets = []
for i in allCombinations:
    counter += 1
    if counter % 1000000 == 0:  # Print every million combinations
        print("Evaluated " + str(counter) + " combinations")
        if len(maxSets) > 0:
            print("Current Average " + str(scoreTotal/len(maxSets))) # Average over time... Should only improve

    # Create a set with the permutation.
    team = Team(players[i[0]], players[i[1]], players[i[2]], players[i[3]], players[i[4]])

    score = get_team_score(team)

    if len(maxSets) < keep_top_n:
        maxSets.append(team)
        scoreTotal += score

    else:
        maxSets.sort(key=get_team_score, reverse=True)
        if get_team_score(maxSets[-1]) < score:
            # Pop Lowest score and replace with a new score...
            s = maxSets.pop()
            scoreTotal -= get_team_score(s)
            maxSets.append(team)
            scoreTotal += score

i=1
maxSets.sort(key=get_team_score, reverse=True)
for s in maxSets:
    print("Team Number " + str(i) + "\tScore: " + str(get_team_score(s)))
    print(s.to_string())
    i += 1
    print("\n")

