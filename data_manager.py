import pandas as pd
from utils import exception_handler


@exception_handler
def load_data(url: str):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        return pd.DataFrame()


@exception_handler
def get_items_above_q1(df: pd.DataFrame, category: str):
    q1 = df[category].quantile(0.1)
    low_quantity_df = df[df[category] < q1]

    return low_quantity_df


