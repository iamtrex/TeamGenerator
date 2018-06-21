from data import Role as R
from model import Player as P, Synergy as S

"""
Constants for data.
"""

#####################################################################################
# Player Configuration
#####################################################################################
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
# Teamwork stuff - Comms, flexibility, untiltability, consistency, each out of 5.
Andrew = P.Player("Andrew", [1, 2, 3, 2, 3], [R.LGo, R.MGo, R.LPl, R.MGo, R.LPl], [3, 3, 4, 4])
Rex = P.Player("Rex", [1, 3, 3, 3, 2], [R.LGo, R.HPl, R.HGo, R.LPl, R.HGo], [5, 3, 2, 4])
Fred = P.Player("Fred", [1, 1, 3, 2, 3], [R.HSi, R.HSi, R.HGo, R.LGo, R.MGo], [2, 5, 4, 3])
Justin = P.Player("Justin", [1, 2, 2, 3, 3], [R.LGo, R.HGo, R.LGo, R.LPl, R.HGo], [3, 3, 2, 3])
Josh = P.Player("Josh", [1, 2, 3, 3, 3], [R.MGo, R.MGo, R.HGo, R.HPl, R.LPl], [3, 4, 2, 3.5])
Jackie = P.Player("Jackie", [3, 3, 3, 1, 2], [R.HGo, R.HGo, R.MGo, R.LGo, R.LGo], [2, 5, 2, 3])
Charles = P.Player("Charles", [3, 1, 2, 2, 3], [R.HGo, R.HSi, R.LGo, R.MGo, R.MGo], [5, 4, 2, 3])
Jason = P.Player("Jason", [1, 3, 2, 2, 3], [R.HSi, R.HGo, R.LGo, R.HSi, R.LGo], [2, 4, 3, 4])
Victor = P.Player("Victor", [3, 1, 3, 3, 2], [R.LGo, R.HSi, R.MGo, R.MGo, R.HSi], [3, 3, 4, 3])
Tyson = P.Player("Tyson", [2, 1, 3, 1, 3], [R.LGo, R.HSi, R.LGo, R.HSi, R.MGo], [2, 4, 2, 3])
Hailin = P.Player("Hailin", [3, 1, 2, 3, 2], [R.LDi, R.HSi, R.LDi, R.LDi, R.HPl], [2, 4, 3, 4])

players = [Andrew, Rex, Fred, Justin, Josh, Jackie, Charles, Jason, Victor, Hailin]

# Setup all the players
corr_map = {
    "Andrew": {S.Synergy(Jackie, -0.1), S.Synergy(Justin, 0.5)},
    "Rex": {S.Synergy(Jackie, -0.5), S.Synergy(Andrew, 0.1)},
    "Fred": {S.Synergy(Josh, 0.1), S.Synergy(Rex, 0.1)},
    "Justin": {S.Synergy(Tyson, -1.0)},
    "Josh": {S.Synergy(Rex, -0.1)},
    "Jackie": {},
    "Charles": {S.Synergy(Victor, 0.1), S.Synergy(Tyson, 0.1)},
    "Jason": {S.Synergy(Jackie, -0.2), S.Synergy(Andrew, 0.1), S.Synergy(Rex, 0.1)},
    "Victor": {S.Synergy(Tyson, 0.5)},
    "Tyson": {},
    "Hailin":{S.Synergy(Rex, 0.1), S.Synergy(Charles, 0.1)}
}

AVG_RANK = R.LPl
MAX_ROLE_PREF = 30

OG = list(range(len(players)))  # The permutations.

# Weights: overall rank, pref roles, level diff, correlatabilities bonus, player stats
weight_factors = [0.45, 0.05, 0.30, 0.1, 0.1]

value_weight = [0.70, 0.30]  # Weight of player's rank vs other stats for their overall value.