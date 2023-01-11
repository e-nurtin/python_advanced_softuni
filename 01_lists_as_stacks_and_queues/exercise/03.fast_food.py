available_food = int(input())

orders = [int(x) for x in input().split()]
orders_queue = orders.copy()
print(max(orders))

for order in orders:
    if available_food >= order:
        available_food -= order
        orders_queue.remove(order)
    else:
        break

if orders_queue:
    print(f"Orders left: {' '.join([str(x) for x in orders_queue])}")
else:
    print("Orders complete")
