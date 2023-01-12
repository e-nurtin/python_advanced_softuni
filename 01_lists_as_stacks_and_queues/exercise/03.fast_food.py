from _collections import deque

available_food = int(input())
orders = [int(x) for x in input().split()]

orders_queue = deque(orders)
print(max(orders))

while orders_queue:
    
    if available_food >= orders_queue[0]:
        current_order = orders_queue.popleft()
        available_food -= current_order
        
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders_queue])}")
        break
else:
    print("Orders complete")
