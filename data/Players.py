from data import Role as R
class Player:

    def __init__(self, name, rolePref, rating, stats):
        self.name = name
        self.rolePref = rolePref
        self.rating = rating
        self.overElo = sum(rating)/len(rating)
        self.stats = stats
        self.flexibility = sum(rolePref)/len(rolePref)


        rating_value = 0
        for i in range(0, 5):
            rating_value += rolePref[i] * rating[i]
        rating_value = rating_value/sum(rolePref) / R.LPl # Average Low plat is already strong!

        self.comms_value = stats[0]/5
        self.flex_value = stats[1]/5
        self.untilt_value = stats[2]/5
        self.consist_value = stats[3]/5
        other_stats_value = sum(stats) / len(stats) / 5  # Even weights for now..., 1.0 is perfect player lol

        self.value = rating_value*0.7+ other_stats_value*0.3  # Get Proper Average


    def total(self):
        return self.flexibility

