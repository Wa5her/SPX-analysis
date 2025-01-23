## Steps to get the Code setup 
1. Run get-qtrly-data.py to output json files in qtrly-data folder
2. Run extract-metrics.py to pull metrics in metrics_to_extract.json into extracted_data.csv
3. Run get-daily-data.py to get csv files of daily stock price in daily-data folder 
4. transform_data.ipynb then builds the training data by blending the collected infromation
5. prepare_ML.ipynb takes the Training data set and runs a regression algorithm 

# Issues to fix:
1. Scaling is done for all variables in the same way. need to customise it better

# Signals to collect:
* Macro economic metrics - consumer confidence, labour participation 
* Banking system metrics - GDP, Repo rate 

# Variables to optimise :
* past results for previous delcaration to SEC
* Other metrics from quaterly results 
* Industry and sector attributes and performance average
* FEature extraction from stock price data
* Feature engineering alternatives to PCA