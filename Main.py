from searchs import RealBestTeams as Brute, TeamGenSearch as Search, PlayerValue as PlayerVal
from data import Const as C
from model import TeamSet as TS

#####################################################################################
# Config Constants
#####################################################################################
keep_top_n = 5  # Keeps top n teams...


#####################################################################################
# Calculation Types...
#####################################################################################

def calc_player_values():
    print("Calculating each player's individual value")
    PlayerVal.calc_and_print_player_value(C.players)


def brute_force_team_sets():
    print("Calculating most balanced teams via Brute Force")
    max_sets = Brute.calc_best_n_team_sets(keep_top_n)
    print_list_ts(max_sets)


def brute_single_teams():
    print("Calculating the best single teams via Brute Force")
    teams = Brute.calc_best_n_teams(keep_top_n)
    print_list_ts(teams)


def print_list_ts(team_sets):
    counter = 1
    for ts in team_sets:
        s = "Team " + str(counter) + " Score " + str(ts.score) + "\n" + \
            ts.to_string() + "\n" + ts.detailed_score()
        counter += 1
        print(s)


def search_team_sets():
    best_team_sets = Search.calc_best_team_sets(keep_top_n)
    print_list_ts(best_team_sets)

#####################################################################################
# Script Start
#####################################################################################

if __name__ == "__main__":
    calc_player_values()
    # brute_force_team_sets()
    # brute_single_teams()
    search_team_sets()

    print("My custom teams")
    # My Custom Team(s)
    my_set = TS.TeamSet(C.Charles, C.Rex, C.Victor, C.Josh, C.Tyson, C.Jackie, C.Jason, C.Fred, C.Justin, C.Andrew)
    my_set_2 = TS.TeamSet(C.Charles, C.Jackie, C.Fred, C.Justin, C.Andrew, C.Victor, C.Jason, C.Rex, C.Josh, C.Tyson)
    my_set_3 = TS.TeamSet(C.Charles, C.Jason, C.Rex, C.Justin, C.Andrew, C.Hailin, C.Jackie, C.Victor, C.Josh, C.Fred)
    print_list_ts([my_set, my_set_2, my_set_3])


