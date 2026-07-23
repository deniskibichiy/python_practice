recent_orders = [15.99, 28.50, 42.75, 18.99, 55.00, 31.25, 22.99, 67.50]

smallest_order = min(recent_orders)

largest_order = max(recent_orders)

total_revenue = round(sum(recent_orders), 2)

average = round(total_revenue/len(recent_orders), 2)

print(f"Smallest order: {smallest_order}")
print(f"Largest order: {largest_order}")
print(f"Total revenue: {total_revenue}")
print(f"Average value of order: {average}")
