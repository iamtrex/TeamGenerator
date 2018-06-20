# TeamGenerator

A Flexible Team Generating Script written in Python.

TeamGenerator takes a set of valid players and attempts to generate two
teams that provide the highest competitive value; that is, the two teams
are similarly skilled (evenly matched), but each are overall as skilled
as possible.

Currently has two methods:

   * AI-based via Local Random Search
        * Pros -> Faster, can be stopped at any time (Finds a decent solution quickly)
        * Cons -> No guarantee of optimal solution found
   * Brute-Force
        * Pros -> Guarantees optimal solution when found.
        * Cons -> Slow (Grows Exponentially as players/data increases)

It takes into account a variety of factors such as
   * Competitive score (how evenly matched two teams are)
   * Overall score (how strong each team is)
   * Player Synergy (or negative synergy) with particular players
   * Player ability at particular roles
   * Player preference at particular roles
   * Other "soft skills" ie communication
   * Varying weights for different components


Other Features

   * Rank players based off of net worth
   * Create a single best team (optimizes players for each position)
   * Flexible -> Can be easily rewritten for other systems.


Currently designed for creating 2 teams with 5 players each for
    League of Legends (or similar 5 player team games), but can be
    easily optimized for all styles of games and varieties.

