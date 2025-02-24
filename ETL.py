import os
import pandas as pd
import json
import xml.etree.ElementTree as ET
import logging
from datetime import datetime

import logging
print(logging.__file__)  # Should point to Python's standard library, not your local directory


# Configure logging
log_file = "log_file.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Add a log
logging.info("Logging setup successful!")
print(f"Log file should be at: {log_file}")

# Function to read CSV file
def extract_csv(file_path):
    logging.info(f"Extracting CSV: {file_path}")
    return pd.read_csv(file_path)

# Function to read JSON file
def extract_json(file_path):
    logging.info(f"Extracting JSON: {file_path}")
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]  # Read line by line
    return pd.DataFrame(data)

# Function to read XML file
def extract_xml(file_path):
    logging.info(f"Extracting XML: {file_path}")
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    for element in root:
        row = {child.tag: child.text for child in element}
        data.append(row)

    return pd.DataFrame(data)

# Function to detect file type and process accordingly
def process_files(directory):
    logging.info("Starting ETL process")
    start_time = datetime.now()

    all_dataframes = []

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        try:
            if file.endswith(".csv"):
                logging.info(f"Processing CSV: {file}")
                all_dataframes.append(extract_csv(file_path))

            elif file.endswith(".json"):
                logging.info(f"Processing JSON: {file}")
                all_dataframes.append(extract_json(file_path))

            elif file.endswith(".xml"):
                logging.info(f"Processing XML: {file}")
                all_dataframes.append(extract_xml(file_path))

        except Exception as e:
            logging.error(f"Error processing {file}: {str(e)}")

    # Merge all data
    if all_dataframes:
        final_df = pd.concat(all_dataframes, ignore_index=True)

        # Save to Excel
        output_file = os.path.join(directory, "transformed_data.csv")
        final_df.to_csv(output_file, index=False, engine="openpyxl")

        logging.info(f"Data successfully merged and saved to {output_file}")
    else:
        logging.warning("No valid files found for processing.")

    end_time = datetime.now()
    logging.info(f"ETL process completed in {end_time - start_time}")

# Set directory path (Change this to your actual path)
directory_path = r"C:\Users\vengatakrishnan.rama\Downloads\source"

# Run ETL process
process_files(directory_path)
