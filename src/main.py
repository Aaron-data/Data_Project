import requests
import json
import os
import pandas as pd
from pathlib import Path



file_path = Path("unleashed.json.txt")   # extension irrelevant

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

orders = data["Items"]
orders_df = pd.json_normalize(
    orders, record_path=["SalesOrderLines"], meta=[ "OrderNumber"]
)



orders_df.to_csv("unleashed_orders.csv", index=False)
print(orders_df.head())













