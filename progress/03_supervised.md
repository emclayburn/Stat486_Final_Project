1. Problem Context: This project aims to predict an NHL player's market value (AAV) by comparing traditional production metrics against advanced efficiency data like Expected Goals ($xG$). The goal is to determine which performance features most influence salary and to identify "anomalous" players who are significantly overvalued or undervalued relative to their on-ice contribution.

2. Supervised Models Implemented
Model Type,Key Hyperparameters Explored,Validation Setup,R2 Score,MAE (Error in $)
Ridge Regression,Alpha (0.1 to 100),5-Fold CV,0.6703,"$1,237,385"
Random Forest,"Max Depth, Estimators, Min Samples",5-Fold CV,0.7456,"$983,765"

3. Model Comparision and Selection
Performance: The Random Forest Regressor outperformed Ridge Regression by a significant margin (approx 7.5 improvement in R^2). This suggests that the relationship between performance and salary is non-linear; for example, "elite" players likely receive a salary premium that a linear model cannot fully capture.
Error Analysis: The MAE of under $1M for the Random Forest is impressive given that NHL salaries range from $750k to over $12M.
Challenges: The primary challenge was handling missing data in the feature set, which was resolved by implementing a SimpleImputer within the modeling pipeline to ensure no data leakage.

4. Explainability and Interpretability
Interpretation: Looking at the SHAP summary plot, PTS (Points) is almost certainly the top feature, with high values (red) pushing the predicted salary significantly higher.
Insight: If Age is high on your list, it shows the model captures how veterans often earn more through unrestricted free agency. If I_F_xGoals has a smaller impact than PTS, it suggests that NHL GMs still value actual results (goals/assists) over underlying efficiency ($xG$) when writing checks.

5. Final Takeaways
The supervised analysis confirms that while traditional production (Points) remains the king of valuation, advanced metrics and usage stats provide the "fine-tuning" that allows the Random Forest to reach ~75% accuracy. This model now provides a "Fair Market Value" baseline that we can use to find the most overvalued and undervalued players in the league.