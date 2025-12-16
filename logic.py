MAX_DAILY_CAPACITY = 200

def decide_order(order, inventory, daily_used):
    qty = order["Quantity"]
    stock = inventory.get(order["ProductCode"], 0)
    priority = order["Priority"]

    if stock <= 0:
        return "Escalate", "No stock available"

    if qty > stock:
        if stock > 0:
            return "Split", f"Only {stock} units available, split required"
        return "Delay", "Insufficient stock"

    if daily_used + qty > MAX_DAILY_CAPACITY:
        if priority == "Urgent" and daily_used < MAX_DAILY_CAPACITY:
            return "Split", "Urgent order partially fits daily capacity"
        return "Delay", "Daily production capacity exceeded"

    return "Approve", "Stock and capacity available"
