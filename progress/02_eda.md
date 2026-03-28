My research question is how well can NHL player performance metrics predict a player’s market value (salary), and which players are significantly overvalued or undervalued relative to their on-ice production?

Dataset: My data comes directly from MoneyPuck.com, a site that tracks data for every NHL game and it publically available. They only thing that they ask is that you clearly credit them for the data, which I will do. There is a lot of data in the dataset, data for different types of situations, Xgoals, position, team, player, shifts, and many other deeper analytical statistics. I also got data directly from Kaggle that shows player statistics and contract numbers. Both sets of data are from the 2024-25 season. This dataset is legally and ethically appropriate as it consists of publicly available professional sports statistics and salary information. No Private Identifiable Information is included, and the analysis is for academic exploratory purposes only.

Target Variable: AAV (Average Annual Value): This is the continuous numeric variable representing the player's yearly salary cap hit, which we are attempting to predict.

Key Predictor Variables:

Production: G (Goals), A (Assists), and PTS (Total Points). These are the traditional "box score" stats that GMs historically use to determine pay.

Usage: ATOI.min (Average Time on Ice in minutes). This represents a player's role; top-paid players almost always log more minutes.

Advanced Efficiency: I_F_xGoals (Individual Expected Goals). This MoneyPuck metric filters out "luck" and shows how many goals a player should have scored based on shot quality.

Possession: onIce_corsiPercentage. This indicates whether the team controls the puck more often than not when this player is on the ice.

Physicality/Defense: BLK (Blocked Shots) and HIT (Hits). Essential for valuing "Defensive Specialists" who don't score much but still earn high salaries.

Preprocessing Completed:

Merging: Combined the MoneyPuck performance CSV with the Kaggle contract CSV using Player.ascii and name as join keys.

Filtering: Removed goaltenders (Pos.grouped != 'G') since their performance metrics (save %, GAA) are entirely different from skaters.

Cleaning: Standardized team names (e.g., ensuring "NYR" and "New York Rangers" matched) and handled missing values in the AAV column (dropped rows where contract data was unavailable).

Feature Engineering: Converted time-based columns into float minutes for easier correlation analysis.