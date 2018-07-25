from searchs import RealBestTeams as Brute, TeamGenSearch as Search, PlayerValue as PlayerVal
from data import Const as C
from model import TeamSet as TS
from evaluation import WinPercentCalculator as WPC

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
    print_list_t(teams)


def print_list_t(team):
    counter = 1
    for t in team:
        s = "Team " + str(counter) + " Score " + str(t.score) + "\n" + \
            t.to_string() + "\n" + t.detailed_score()
        counter += 1
        print(s)

def print_list_ts(team_sets):
    counter = 1
    for ts in team_sets:
        s = "Team " + str(counter) + " Score " + str(ts.score) + "\n" + \
            ts.to_string() + "\n" + ts.detailed_score()

        print(s)
        print("WinRate my set " + str(counter) + " " + str(WPC.team1_win_rate(ts)))
        print()  # Blank line.
        counter += 1


def search_team_sets():
    best_team_sets = Search.calc_best_team_sets(keep_top_n)
    print_list_ts(best_team_sets)

#####################################################################################
# Script Start
#####################################################################################

if __name__ == "__main__":
    calc_player_values()
    # brute_force_team_sets()
    brute_single_teams()
    search_team_sets()



    '''
    print("My custom teams")
    # My Custom Team(s)
    my_set = TS.TeamSet(C.Charles, C.Rex, C.Victor, C.Josh, C.Tyson, C.Jackie, C.Jason, C.Fred, C.Justin, C.Andrew)
    my_set_2 = TS.TeamSet(C.Charles, C.Jackie, C.Fred, C.Justin, C.Andrew, C.Victor, C.Jason, C.Rex, C.Josh, C.Tyson)
    my_set_3 = TS.TeamSet(C.Charles, C.Jason, C.Rex, C.Justin, C.Andrew, C.Hailin, C.Jackie, C.Victor, C.Josh, C.Fred)
    uneven_set = TS.TeamSet(C.Hailin, C.Rex, C.Fred, C.Josh, C.Andrew, C.Tyson, C.Victor, C.Jason, C.Charles, C.Jackie)
    july21_set = TS.TeamSet(C.Charles, C.Jason, C.Fred, C.Justin, C.Andrew, C.Jackie, C.Rex, C.Victor, C.Josh, C.Vincent)
    july21_set2 = TS.TeamSet(C.Charles, C.Rex, C.Fred, C.Justin, C.Andrew, C.Jackie, C.Jason, C.Victor, C.Josh,C.Vincent)
    july21_set3 = TS.TeamSet(C.Charles, C.Jason, C.Fred, C.Josh, C.Vincent, C.Jackie, C.Rex, C.Victor, C.Justin, C.Andrew)
    july21_set4 = TS.TeamSet(C.Charles, C.Rex, C.Victor, C.Josh, C.Vincent, C.Jackie, C.Jason, C.Fred, C.Justin, C.Andrew)

    july21_actual = TS.TeamSet(C.Andrew, C.Rex, C.Fred, C.Josh, C.Vincent, C.Charles, C.Jason, C.Victor, C.Justin, C.Tyson)

    my_sets = [my_set, my_set_2, my_set_3, uneven_set, july21_set, july21_set2, july21_set3, july21_set4, july21_actual]

    print_list_ts(my_sets)

    
    counter = 1
    for i in my_sets:
        print("WinRate my set " + str(counter) + " " + str(WPC.team1_win_rate(i)))
        
        counter += 1

    '''



