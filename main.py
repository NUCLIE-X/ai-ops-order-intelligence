import csv
from collections import defaultdict
from logic import decide_order

inventory = {}
daily_capacity = defaultdict(int)

with open("inventory.csv") as f:
    for row in csv.DictReader(f):
        inventory[row["ProductCode"]] = int(row["AvailableStock"])

print("\nAI OPS ORDER DECISIONS\n")

with open("orders.csv") as f:
    for order in csv.DictReader(f):
        order["Quantity"] = int(order["Quantity"])
        date = order["OrderDate"]

        decision, reason = decide_order(order, inventory, daily_capacity[date])

        if decision in ["Approve", "Split"]:
            used = min(order["Quantity"], inventory[order["ProductCode"]])
            inventory[order["ProductCode"]] -= used
            daily_capacity[date] += used

        print(f"{order['OrderID']} | {decision} | {reason}")
