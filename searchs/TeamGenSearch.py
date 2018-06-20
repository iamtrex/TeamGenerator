from data import Const as C
from model import TeamSet as TS

import random
import time

"""
AI Generative Search for Best Team(s). 
"""

SEARCH_DURATION = 500000  # Number of steps to do calculations for -> 1 million

POP_SIZE = 10
PROB_RANDOM_SET = 0.10
PROB_RANDOM_MUTATION = 0.40
PROB_RANDOM_SWAP = 0.80
SAVE_EVERY_N = 1  # Save top teams every N...
PERSISTENT_FEEDBACK_EVERY_N = 10000  # Print current record holder every N


def get_score(obj):
    return obj.score


def create_random_team_set():
    i = random.sample(C.OG, 10)
    return TS.TeamSet(C.players[i[0]], C.players[i[1]], C.players[i[2]], C.players[i[3]], C.players[i[4]],
                        C.players[i[5]], C.players[i[6]], C.players[i[7]], C.players[i[8]], C.players[i[9]])


def choose_a_set(curr_best_team_sets, total):
    i = random.randint(0, 100)
    score_total = curr_best_team_sets[0].score / total
    choice = 0
    while score_total < i:
        choice += 1
        score_total += curr_best_team_sets[choice].score / total
    return choice


def get_total(curr_best_team_sets):
    total = 0
    for i in curr_best_team_sets:
        total += i.score
    return total


def mutate_one_spot(ts_new_players):
    if len(C.players) <= 10:  # Cannot perform this mutation.
        return

    pos = random.randint(0, 9)
    s1 = set(ts_new_players)
    s2 = set(C.players)
    subs = s2 - s1
    new_player = random.sample(subs, 1)[0]
    ts_new_players[pos] = new_player


def swap_one_spot(ts_new_players):
    pos = random.sample(range(0, 10), 2)
    ts_new_players[pos[0]], ts_new_players[pos[1]] = ts_new_players[pos[1]], ts_new_players[pos[0]]


# def fix_duplicates(ts):
#     ts_fixed = []
#     for i in ts:
#         if i not in ts_fixed:
#             ts_fixed.append(i)
#         else:
#             while i in ts_fixed:
#                 i = C.players[random.sample(C.OG, 10)[0]]
#             ts_fixed.append(i)  # Add a new player.
#     return ts_fixed


def mate_sets(ts1):
    i = random.randint(0, 100)

    # Chance of Random Restart.
    if i <= PROB_RANDOM_SET * 100:
        ts1 = create_random_team_set()
        return ts1

    # Otherwise mate the two sets as expected.
    t1_old = ts1.t1.players
    t2_old = ts1.t2.players

    # "Genetic Mating" between self teams...
    swap_pos = random.randint(0, 4)
    t1_new = t1_old[:swap_pos] + t2_old[swap_pos:]
    t2_new = t2_old[:swap_pos] + t1_old[swap_pos:]

    ts_new_players = t1_new + t2_new

    # Fix Repeats
    # Possible Mutation
    i = random.randint(0, 100)
    if i <= PROB_RANDOM_MUTATION * 100:
        mutate_one_spot(ts_new_players)

    # Random Role Swap
    i = random.randint(0, 100)
    if i <= PROB_RANDOM_SWAP * 100:
        swap_one_spot(ts_new_players)

    ts = TS.TeamSet(*ts_new_players)
    return ts


def create_option_set(curr_best_team_sets, total):
    my_list = []

    for i in curr_best_team_sets:
        my_list = my_list + [i] * int(round(i.score/total*100))
    return my_list


def calc_best_team_sets(n):
    all_time_best = []
    last_best = None

    time_start = time.time()
    iter = 1
    curr_best_team_sets = []

    high_score = 0
    # Create the starting population randomly:
    for i in range(0, POP_SIZE):
        ts = create_random_team_set()
        score = ts.score
        if score > high_score:
            high_score = score
        curr_best_team_sets.append(ts)

    while iter < SEARCH_DURATION:
        # Select the children...

        if len(all_time_best) > 0 and all_time_best[0] not in curr_best_team_sets:  # Keep an extra spot for all time best...
                                                            # Increase likelihood of improvement on it...
            curr_best_team_sets.append(all_time_best[0])

        total = get_total(curr_best_team_sets)
        option_set = create_option_set(curr_best_team_sets, total)

        choices = []
        while len(choices) < POP_SIZE:
            choices.append(random.sample(option_set, 1)[0])

        # Mate children, with potential crossover.
        next_generation = []
        while len(choices) > 0:
            old_ts = choices.pop()
            new_ts = mate_sets(old_ts)
            next_generation.append(new_ts)

        curr_best_team_sets = next_generation

        if iter % SAVE_EVERY_N == 0:  # Save every nth iteration...
            sorted_sets = (all_time_best + curr_best_team_sets)
            sorted_sets.sort(key=get_score, reverse=True)
            all_time_best = sorted_sets[:n]  # Keep top N.

        if iter % PERSISTENT_FEEDBACK_EVERY_N == 0:
            print("Iteration number " + str(iter) + " - Score " + str(all_time_best[0].score) +
                  "\nTime Elapsed " + str(round(time.time() - time_start, 3)) + " sec")

            if last_best == all_time_best[0]:
                print("Best Team Unchanged")
            else:
                print(all_time_best[0].to_string())
                last_best = all_time_best[0]

            print()

        iter += 1

    sorted_sets = (all_time_best + curr_best_team_sets)
    sorted_sets.sort(key=get_score, reverse=True)

    print("Time Taken -" + str(time.time()-time_start))

    return sorted_sets[:n]  # Return n best teams.
