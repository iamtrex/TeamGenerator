from data import Const as C
import math
"""
Given TeamSet, calculate winrate.
"""


def team1_win_rate(teamset):
    t1 = teamset.t1
    t2 = teamset.t2

    # Compare Strength in Roles

    role_skill = []

    for i in range(0, 4):  # + number means what % t1's player is above t2's skillwise
        role_skill.append(t1.players[i].rating[i] - t2.players[i].rating[i])

    t1_role_advantage = sum(role_skill) / 5 * 200  # Advantage per role.
    # A 0.2 advantage in each role = L Gold vs L Plat = 90% WR (+ 40%) So scale by 200x

    sum_metrics = 0  # Sum of other metrics, with how much t1 ahead of t2.

    for i in range(C.VAL_COEFF_COUNT):
        sum_metrics += (t1.other_values[i] - t2.other_values[i]) * \
                            C.PLAYER_OTHER_STATS_DIFF_WEIGHTS[i]
    other_metrics = sum_metrics / C.VAL_COEFF_COUNT * 25

    # If better by 1 for each metric overall, then winrate should be increased by at least 25%, so * 25

    return 50 + (t1_role_advantage + other_metrics) / 2  # weight to 50% being even.

