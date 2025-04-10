#importing pandas library
import pandas as pd

# to load customer dataset
def load_data(path="mall_customers.csv"):
    # To read CSV file using pandas
    try:
        df = pd.read_csv(path)
        print("# Data loaded successfully")
        return df
    except Exception as e:
        print("# Error loading data:", e)
        return None
