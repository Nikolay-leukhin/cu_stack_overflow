from data_manager import *
from file_manager import *


df = load_data(url='data/inventory.csv')
df_low_q = get_items_above_q1(df, 'Quantity in Stock')
write_to_df_report(df_low_q, "low_quantity_report.txt")
