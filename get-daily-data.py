import os
import pandas as pd
import yfinance as yf
from datetime import timedelta, datetime

def get_daily_data(input_file='extracted_data.csv',output_folder = 'daily-data'):
    filepath = os.path.join(os.getcwd(), output_folder)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    eps_df = pd.read_csv(input_file,parse_dates=['start','end','filed'])
    
    for ticker in eps_df['ticker'].unique():    
        start = eps_df[eps_df['ticker'] == ticker]['start'].min()
        #end = eps_df[eps_df['ticker'] == ticker]['end'].max()
        end = datetime.today()
        csv_file = os.path.join(filepath,f'{ticker}.csv')

        try:
            if not os.path.exists(csv_file):
                data = yf.download(ticker, start - timedelta(days=3),
                            end + timedelta(days=3), progress=False)
                data.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
                data.to_csv(csv_file, index=False)
                #print("Downloaded data for ", ticker)
        except Exception as e:
            print(e)
            print(f"Failed to download {ticker}")
            continue

if __name__ == "__main__":
    get_daily_data()
