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

Summary Statistics:
Variable,Count,Mean,Std Dev,Min,Median (50%),Max
AAV (Target),880,"$3,053,777","$2,792,083","$750,000","$1,737,500","$14,000,000"
Points (PTS),880,22.14,23.22,0.0,15.0,121.0
xGoals (I_F_xGoals),880,8.98,9.15,0.0,5.62,41.05
Ice Time (sec),880,"51,239","34,669",70.0,"55,339","129,982"
Age,878,27.13,4.33,18.0,27.0,40.0

Key Insights:
Strong Predictors: Total Points (PTS) has the highest correlation with salary (r = 0.75), followed by Points Per Game (0.70) and Ice Time (0.70). This confirms that traditional production and overall usage remain the primary drivers of NHL contracts.
Salary Skewness: The median AAV ($1.7M) is significantly lower than the mean ($3.05M). This indicates a right-skewed distribution where a large portion of the league plays on lower-value contracts, while a small group of "elite" players earn upwards of $10M-$14M.
Advanced Metrics: Expected Goals (I_F_xGoals) shows a strong correlation (0.63), but it is lower than raw points. This suggests the model may identify "anomalies" where players have high expected production but lower salaries/raw point totals.

Visual Exploration:
! [Total Points vs AAV](plot1.png)
Description: This scatter plot shows the relationship between a player's total points and their Annual Average Value (AAV).

Relevance: It confirms a strong positive correlation (r = 0.75), but more importantly, it highlights the "spread." Players in the bottom right (high points, low salary) represent high-value assets, while those in the top left (low points, high salary) may be overvalued. This visualization justifies using regression to find the "expected" salary line and identifying anomalies that fall far from it.

! [Salary Distribution by Position](plot2.png)
Description: This box plot compares the distribution of salaries between Forwards (F) and Defensemen (D).

Relevance: It helps determine if "Position" needs to be a key categorical feature in our supervised model. We can see that while the medians are somewhat similar, Forwards have a higher "ceiling" with more elite-paid outliers. This suggests that the market values high-end scoring (typically forwards) differently than defensive contributions, which will be important for the model to distinguish.

Challenges and Reflection:
Challenge: One of the primary challenges was handling the "Situation" granularity in the MoneyPuck data. Because players are listed multiple times (5on5, Power Play, Penalty Kill, etc.), I had to specifically filter for the "all" situation to ensure each player had a single row representing their total season performance. Additionally, synchronizing player names between the MoneyPuck and Kaggle datasets required string cleaning (lowercasing and trimming) to ensure a high match rate for the merge.

LINKS: https://www.kaggle.com/datasets/natenadeau/nhl-2024-25-statscontacts?resource=download

https://moneypuck.com/data.htm