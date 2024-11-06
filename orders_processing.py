import numpy as np
import pandas as pd
from utils import exception_handler


@exception_handler
def process_order(inventory: pd.DataFrame, item_code: int, quantity_ordered: int, date: str):
    """
    2. **Обработка заказов**
        - Настрой загрузку данных и обновление остатка товаров на складе.
        - Если заказ превышает количество товара на складе, система должна 
        либо частично исполнить заказ, либо отклонить его с логированием 
        (подход выбери самостоятельно).
    """
    
    if item_code not in inventory['Item Code'].values:
        # cancel order
        # logging: item not found
        return None

    if inventory.loc[item_code, 'Quantity in Stock'] < quantity_ordered:
		# cancel order
        # logging: "not enough in stock \nCode: {item_code}, \tName: {inventory.loc[item_code, 'Name']}, \tQuantity: {inventory.loc[item_code, 'Quantity in Stock']}"
        return None
    
    inventory.loc[item_code, 'Quantity in Stock'] -= quantity_ordered
    return inventory
    
@exception_handler
def generate_report(inventory):
    """
    6. **Генерация отчёта**
    - Сформируй отчёт для менеджера:
        - общее количество товаров на складе,
        - товары с критическими запасами,
        - рекомендации по закупкам.
    - Отчёт должен быть сохранен в формате `.txt` и автоматически обновляться ежедневно.
    """
    
    # sort inventory by quantity in stock
    inventory = inventory.sort_values(by=['Quantity in Stock'], ascending=True)
    try:
        with open('report.txt', 'w+') as f:
            f.write(f'Total items in stock: {inventory["Quantity in Stock"].sum()}\n')
            f.write(f'Critical items: {inventory.loc[inventory["Quantity in Stock"] < 100, "Name"].values}\n')
            f.write(f'Recommendations: {inventory.loc[inventory["Quantity in Stock"] < 150, "Name"].values}')
    except Exception as e:
        raise e
    
