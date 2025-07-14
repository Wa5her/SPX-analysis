# SPX Financial Data Analysis

## Project Overview
A personal project to automate the extraction, transformation, and analysis of S&P 500 companies' financial and stock data. The workflow enables the creation of machine learning-ready datasets for fundamental analysis and earnings prediction.

## Setup & Usage Instructions
1. **Extract Quarterly Data:**
   - Run `get-qtrly-data.py` to download and save quarterly financial data as JSON files in the `qtrly-data/` folder.
2. **Extract Metrics:**
   - Run `extract_metrics.py` to pull specified metrics (from `metrics_to_extract.json`) into `extracted_data.csv`.
3. **Download Daily Stock Data:**
   - Run `get-daily-data.py` to fetch daily stock prices and save them as CSV files in the `daily-data/` folder.
4. **Transform Data:**
   - Open and run `transform_data.ipynb` to blend and preprocess the collected data, building the training dataset.
5. **Machine Learning Preparation:**
   - Use `prepare_ML.ipynb` to run regression algorithms and experiment with predictive models on the training data.

## Current Issues / To-Do
- Improve scaling: Currently, all variables are scaled uniformly; implement customized scaling per variable type.

## Signals & Features to Collect
- **Macro-Economic Metrics:**
  - Consumer confidence
  - Labour participation
- **Banking System Metrics:**
  - GDP
  - Repo rate

## Variables & Feature Engineering Ideas
- Past results from previous SEC declarations
- Additional metrics from quarterly results
- Industry and sector attributes and performance averages
- Feature extraction from stock price data
- Explore alternatives to PCA for feature engineering

---
*For questions or suggestions, feel free to reach out!*