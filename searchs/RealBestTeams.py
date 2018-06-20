from data import Const as C
from model import TeamSet as TS, Team as T

import itertools
import time

'''Class Def Player - Represents a Player with name, preferred roles, and rating at each role.'''


def get_score(obj):
    return obj.score


def calc_best_n_team_sets(n):
    # Track Time execution
    time_start = time.time()

    team_sets = []  # List of Sets, keeps top n
    counter = 0
    score_total = 0

    # Create all permutations
    all_combinations = itertools.permutations(C.OG, 10)
    for i in all_combinations:
        counter += 1
        if counter % 1000000 == 0:  # Print every million combinations
            print("Evaluated " + str(counter) + " combinations")
            if len(team_sets) > 0:
                print("Current Average " + str(score_total / len(team_sets)))  # Average over time... Should only improve
                print("Current Best " + team_sets[0].to_string())

        # Create a set with the permutation.
        team_set = TS.TeamSet(C.players[i[0]], C.players[i[1]], C.players[i[2]], C.players[i[3]], C.players[i[4]],
                              C.players[i[5]], C.players[i[6]], C.players[i[7]], C.players[i[8]], C.players[i[9]])

        score = get_score(team_set)

        if len(team_sets) < n:
            team_sets.append(team_set)
            score_total += score

        else:
            team_sets.sort(key=get_score, reverse=True)
            last_place = get_score(team_sets[-1])
            if last_place < score:
                # Pop Lowest score and replace with a new score...
                while last_place < score and len(team_sets) > n:
                    s = team_sets.pop()
                    score_total -= get_score(s)
                    last_place = get_score(team_sets[-1])

                team_sets.append(team_set)
                score_total += score
            elif last_place == score:
                # Append to the end.
                score_total += score
                team_sets.append(team_set)

    # Print Team from Best to Worst
    team_sets.sort(key=get_score, reverse=True)
    print("Time Taken " + str(time.time() - time_start) + "s")
    return team_sets


def calc_best_n_teams(n):
    time_start = time.time()

    counter = 1
    all_combinations = itertools.permutations(C.OG, 5)
    score_total = 0
    teams = []
    for i in all_combinations:
        counter += 1
        if counter % 10000 == 0:  # Print every 1000 combinations
            print("Evaluated " + str(counter) + " combinations")
            if len(teams) > 0:
                print("Current Average " + str(score_total / len(teams)))  # Average over time... Should only improve
                print("Current Best\n" + teams[0].to_string())


        # Create a set with the permutation.
        team = T.Team(C.players[i[0]], C.players[i[1]], C.players[i[2]], C.players[i[3]], C.players[i[4]])

        score = get_score(team)

        if len(teams) < n:
            teams.append(team)
            score_total += score

        else:
            teams.sort(key=get_score, reverse=True)
            last_place = get_score(teams[-1])
            if last_place < score:
                # Pop Lowest score and replace with a new score...
                s = teams.pop()
                score_total -= last_place
                teams.append(team)
                score_total += score
            elif last_place == score:
                # Append to the end.
                score_total += score
                teams.append(team)

    teams.sort(key=get_score, reverse=True)
    print("Time Taken " + str(time.time() - time_start) + "s")
    return teams

