import numpy as np
import pandas as pd


def load_data(url: str):
    df = pd.read_csv(url)
    return df


def write_sold_out_report():
    ...
