from data_manager import *
from file_manager import *
from orders_processing import *


df = load_data(url='data/inventory.csv')
df_low_q = get_items_above_q1(df, 'Quantity in Stock')
write_to_df_report(df_low_q, "low_quantity_report.txt")

days = [5, 6, 7]
for day in days:
    print("Day: ", day)
    orders = load_data(url=f'data/orders_2023-09-0{day}.csv')
    for ind, order in orders.iterrows():
        print(order)
        # if not process_order(df, *order):
        #     print("")
    # generate_report(df)
