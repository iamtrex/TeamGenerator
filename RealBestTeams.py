from data import Const as C
from data import Team as T
from data import TeamSet as TS

import itertools
import time

'''Class Def Player - Represents a Player with name, preferred roles, and rating at each role.'''


def get_value(player):
    return player.value


def get_score(obj):
    return obj.score


def print_team_set(ts, num):
    print("Team Number " + str(num) + "\tScore: " + str(get_score(ts)))
    print(ts.to_string())
    print("\n")


def calc_best_n_team_sets(n):
    # Track Time execution
    time_start = time.time()

    team_sets = []  # List of Sets, keeps top n
    counter = 0
    score_total = 0

    # Create all permutations
    all_combinations = itertools.permutations(og, 10)
    for i in all_combinations:
        counter += 1
        if counter % 1000000 == 0:  # Print every million combinations
            print("Evaluated " + str(counter) + " combinations")
            if len(team_sets) > 0:
                print("Current Average " + str(score_total / len(team_sets)))  # Average over time... Should only improve

        # Create a set with the permutation.
        team_set = TS.TeamSet(C.players[i[0]], C.players[i[1]], C.players[i[2]], C.players[i[3]], C.players[i[4]],
                              C.players[i[5]], C.players[i[6]], C.players[i[7]], C.players[i[8]], C.players[i[9]])

        score = get_score(team_set)

        if len(team_sets) < n:
            team_sets.append(team_set)
            score_total += score

        else:
            team_sets.sort(key=get_score, reverse=True)
            if get_score(team_sets[-1]) < score:
                # Pop Lowest score and replace with a new score...
                s = team_sets.pop()
                score_total -= get_score(s)
                team_sets.append(team_set)
                score_total += score

    # Print Team from Best to Worst
    team_sets.sort(key=get_score, reverse=True)
    print("Time Taken " + str(time.time() - time_start) + "s")
    return team_sets


def calc_best_n_teams(n):
    time_start = time.time()

    counter = 1
    all_combinations = itertools.permutations(og, 5)
    score_total = 0
    teams = []
    for i in all_combinations:
        counter += 1
        if counter % 100000 == 0:  # Print every 100000 combinations
            print("Evaluated " + str(counter) + " combinations")
            if len(teams) > 0:
                print("Current Average " + str(score_total / len(teams)))  # Average over time... Should only improve

        # Create a set with the permutation.
        team = T.Team(C.players[i[0]], C.players[i[1]], C.players[i[2]], C.players[i[3]], C.players[i[4]])

        score = get_score(team)

        if len(teams) < n:
            teams.append(team)
            score_total += score

        else:
            teams.sort(key=get_score, reverse=True)
            if get_score(teams[-1]) < score:
                # Pop Lowest score and replace with a new score...
                s = teams.pop()
                score_total -= get_score(s)
                teams.append(team)
                score_total += score

    teams.sort(key=get_score, reverse=True)
    print("Time Taken " + str(time.time() - time_start) + "s")
    return teams


def calc_player_value(players):
    print("Player Values\n")
    total_value = 0
    for p in players:
        total_value += p.value

    avg = round(total_value / len(players), 5)
    players.sort(key=get_value)
    for p in players:
        print(p.name + "\t" + str(round((p.value - avg) / avg, 3)))

#####################################################################################
# Player Configuration
#####################################################################################
# Setup Initial


#####################################################################################
# Config Constants
#####################################################################################
keep_top_n = 5  # Keeps top n teams...
og = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # The permutations.


#####################################################################################
# Script Start
#####################################################################################
print("Calculating each player's individual value")
calc_player_value(C.players)

print("Calculating most balanced teams")
max_sets = calc_best_n_team_sets(keep_top_n)
i = 1
for s in max_sets:
    print_team_set(s, i)
    i += 1

print("My personal teams")
# My Custom Team(s)
my_set = TS.TeamSet(C.Charles, C.Rex, C.Victor, C.Josh, C.Tyson, C.Jackie, C.Jason, C.Fred, C.Justin, C.Andrew)
print_team_set(my_set, "MyTeam 1")
my_set_2 = TS.TeamSet(C.Charles, C.Jackie, C.Fred, C.Justin, C.Andrew, C.Victor, C.Jason, C.Rex, C.Josh, C.Tyson)
print_team_set(my_set_2, "MyTeam 2")


i = 1
print("Calculating the best single team(s)")
teams = calc_best_n_teams(keep_top_n)
for s in teams:
    print("Team Number " + str(i) + "\tScore: " + str(get_score(s)))
    print(s.to_string())
    i += 1
    print("\n")

