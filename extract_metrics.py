import json
import os
import pandas as pd

def extract_metrics(metrics_and_units, directory="./qtrly-data"):
    """
    Extracts specified metrics and their units from JSON files in the current directory.

    Args:
        metrics_and_units: A dictionary where keys are metric names 
                           and values are their corresponding units.

    Returns:
        A pandas DataFrame containing the extracted data.
    """
    data = []
    # current_directory = os.getcwd()

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            ticker = os.path.splitext(filename)[0]

            try:
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                    us_gaap_elements = json_data.get(
                        'facts', {}).get('us-gaap', {})

                    for metric, unit in metrics_and_units.items():
                        metric_data = us_gaap_elements.get(
                            metric, {}).get('units', {})
                        if unit in metric_data:
                            for entry in metric_data[unit]:
                                entry_data = {
                                    'ticker': ticker, 'metric': metric}
                                entry_data.update(entry)
                                data.append(entry_data)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {filename}: {e}")

    return pd.DataFrame(data)

if __name__ == "__main__":
    with open('metrics_to_extract.json', 'r') as file:
        metrics_and_units = json.load(file)

    extracted_data = extract_metrics(metrics_and_units)
    #print(extracted_data.head())
    extracted_data.to_csv('extracted_data.csv', index=False)