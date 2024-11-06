import pandas as pd
from utils import log_exception


@log_exception
def load_data(url: str):
    df = pd.read_csv(url)
    return df


@log_exception
def get_items_above_q1(df: pd.DataFrame, category: str):
    q1 = df[category].quantile(0.1)
    low_quantity_df = df[df[category] < q1]

    return low_quantity_df


