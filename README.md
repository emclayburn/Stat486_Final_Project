# Stat486_Final_Project

# Stat486_Final_Project

This project uses machine learning to predict NHL player salaries (AAV) based on performance metrics from the 2024-25 season. It identifies market inefficiencies by flagging "Underpaid" and "Overpaid" players relative to their on-ice production.

# Reproducibility Instructions
To reproduce the analysis and the final model, follow these steps in order:

### Environment Setup
Ensure you have Python 3.9+ installed, then install the required dependencies:

```Bash
pip install -r requirements.txt
```

### Execution Order
Run the following files in this exact sequence to regenerate the results:

#### notebooks/exploration.ipynb: 
Handles initial data loading, cleaning, and the 15-game minimum filtering. It produces the summary statistics and correlation matrices.

#### notebooks/models.ipynb:

- Trains the Ridge Regression and Random Forest models.

- Performs Hyperparameter Tuning via 5-Fold Cross-Validation.

- Generates the SHAP interpretability plots.

- Runs the k-Means Clustering analysis.

- Output: Saves the final model to src/rf_model.pkl and predictions to data/valuation_results.csv.

#### src/app.py: 
Launches the Streamlit interface to interact with the model results.

# Main Results
#### Supervised Performance: 
Our Random Forest model achieved an R^2 of 0.72, with Ice Time and Points Per Game serving as the most influential predictors.
#### Market Insights: 
We identified 4 distinct player archetypes using clustering. The analysis highlights a significant "Superstar Premium" where elite players earn ~$4M+ above their predicted statistical value.

# Data Sources

#### Performance Stats: 
MoneyPuck (2024-25 Skater Data).

Salary Data: Compiled 2025-26 contract data via Kaggle.