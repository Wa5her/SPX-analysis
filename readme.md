Run get-qtrly-data.py to pull data from all SEC filings of companies listed in the S&P 500 index.

### Requirements:
* Python 3
* Pandas

### Usage:
```bash
python get-qtrly-data.py
```

Change metrics-to-extract.json to choose the metrics you want to pull from all these files. The basic config pulls information about EPS. 

Run extract-metrics.py to extract the data from the downloaded files and save it in a csv file extracted_data.csv.

Run get-daily-data.py to pull daily data for each of the companies listed in the S&P 500 index for the range of time in the extracted_data.csv file.

### Requirements:
* Python 3
* Pandas

### Usage:
```bash
python get-daily-data.py
```

Change metrics-to-extract.json to choose the metrics you want to pull from all these files. The basic config pulls information about EPS.