import RealBestTeams as Brute
import TeamGenSearch as Search
from data import Const as C
from model import TeamSet as TS

#####################################################################################
# Config Constants
#####################################################################################
keep_top_n = 5  # Keeps top n teams...


#####################################################################################
# Script Start
#####################################################################################

def calc_player_values():
    print("Calculating each player's individual value")
    Brute.calc_player_value(C.players)

def brute_force_team_sets():
    print("Calculating most balanced teams")
    max_sets = Brute.calc_best_n_team_sets(keep_top_n)
    i = 1
    for s in max_sets:
        Brute.print_team_set(s, i)
        i += 1

    print("My personal teams")
    # My Custom Team(s)
    my_set = TS.TeamSet(C.Charles, C.Rex, C.Victor, C.Josh, C.Tyson, C.Jackie, C.Jason, C.Fred, C.Justin, C.Andrew)
    Brute.print_team_set(my_set, "MyTeam 1")
    my_set_2 = TS.TeamSet(C.Charles, C.Jackie, C.Fred, C.Justin, C.Andrew, C.Victor, C.Jason, C.Rex, C.Josh, C.Tyson)
    Brute.print_team_set(my_set_2, "MyTeam 2")

def brute_single_teams():
    i = 1
    print("Calculating the best single team(s)")
    teams = Brute.calc_best_n_teams(keep_top_n)
    for s in teams:
        print("Team Number " + str(i) + "\tScore: " + str(Brute.get_score(s)))
        print(s.to_string())
        i += 1
        print("\n")

def search_team_sets():
    best_team_sets = Search.calc_best_team_sets(keep_top_n)
    for ts in best_team_sets:
        print(ts.to_string())

if __name__ == "__main__":
    # calc_player_values()
     brute_force_team_sets()
    # brute_single_teams()
    # search_team_sets()

