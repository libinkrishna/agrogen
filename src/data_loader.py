import pandas as pd

def load_data(filepath):
    print(f"Loading data from {filepath}")
    data = pd.read_csv(filepath)
    return data
