
"""
Calculates Player Values

"""


def get_value(player):
    return player.value


# Given a pool of players, calculates their value and ranks them fit to a mean.
def calc_and_print_player_value(players):
    print("Player Values\n")
    total_value = 0
    for p in players:
        total_value += p.value

    avg = round(total_value / len(players), 5)
    players.sort(key=get_value, reverse=True)
    for p in players:
        print(p.name + "\t" + str(round((p.value - avg) / avg, 3)))



#####################################################################################
#
#####################################################################################