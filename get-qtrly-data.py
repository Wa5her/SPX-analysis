import json
from time import sleep
import pandas as pd
import requests
import os
from io import StringIO
# import multiprocessing



# function for downloading files from SEC
def download_file(url, filename, user_agent="Michelle LiuWatts admin@hercompany.com"):
    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers)
    sleep(0.101)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        return f"File downloaded successfully as {filename}"

    else:
        print(f"Failed to download {url}: {response.status_code}")
        return False
def is_valid_json(filepath):
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError:
        return False
def _main():
    # URL of the Wikipedia page
    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    

    # Read the tables on the Wikipedia page
    response = requests.get(wiki_url)
    tables = pd.read_html(StringIO(response.text))

    # The first table on the page contains the S&P 500 companies
    sp500_table = tables[0]

    new = exist = failed = 0
    save_dir = os.path.join(os.getcwd(), "qtrly-data")

    # with multiprocessing.Pool(4) as pool:
    #     pool.apply_async(download_file, (url, filepath))

    for i, row in sp500_table.iterrows():
        cik = str(row['CIK']).zfill(10)
        ticker = row['Symbol']

        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
        filepath = os.path.join(save_dir, f"{ticker}.json")

        if not os.path.exists(filepath):

            result = download_file(url, filepath)

            new = new + 1

        else:
            if is_valid_json(filepath):
                result = f"{ticker} already downloaded"
                exist = exist + 1
            else:
                result = download_file(url, filepath)
                new = new + 1

            # print(result)

        if not result:

            print(f"{ticker} failed to download")

            failed = failed + 1

    print(f"Downloaded {new} new files, {exist} files already existed, and {failed} files failed to download")
        

if __name__ == "__main__":
    _main()