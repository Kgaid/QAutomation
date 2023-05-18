import json

with open('manager_sales.json') as f:
    data = json.load(f)

sales_sum_by_manager = {}
for manager in data:
    manager_name = f"{manager['manager']['first_name']} {manager['manager']['last_name']}"
    sales = sum(cars['price'] for cars in manager['cars'])
    if manager_name in sales_sum_by_manager:
        sales_sum_by_manager[manager_name] += sales
    else:
        sales_sum_by_manager[manager_name] = sales

best_manager = max(sales_sum_by_manager, key=sales_sum_by_manager.get)
total_sales = sales_sum_by_manager[best_manager]

print(f"The best manager: {best_manager} with sales: {total_sales}")
