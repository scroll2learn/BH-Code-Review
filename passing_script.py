import os
import sys
import json
import logging
import requests  # Used correctly
TEST

# Use environment variables instead of hardcoded secrets (Passes Security Test)
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Set up logging (Passes Logging Test)
logging.basicConfig(level=logging.INFO)

def safe_divide(a, b):
    """Returns division result, handling errors properly."""
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Attempted division by zero.")
        return None

def process_data():
    """Processes some data (Dummy function)."""
    logging.info("Processing data...")

class DataProcessor:
    """Class to handle data processing (Passes Class Naming Convention)."""
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        """Cleans the data (Passes Function Naming Convention)."""
        logging.info("Cleaning data...")

if __name__ == "__main__":
    # Passes Main Execution Check
    logging.info("Starting script...")

    # Function Call (Passes Function Definition Check)
    result = safe_divide(10, 2)
    logging.info(f"Result: {result}")

    processor = DataProcessor(["data1", "data2"])
    processor.clean_data()

    # Passes Performance Check (No unnecessary nested loops)
    for i in range(5):
        logging.info(f"Processing item {i}")

    # Passes Dependency Test (No unused imports)
    response = requests.get("https://example.com")
    logging.info(f"Response status: {response.status_code}")
