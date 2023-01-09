def check_water(needed, tank_water):
    if needed <= tank_water:
        print(f"{list_of_queue.pop(0)} got water")
        tank_water -= needed
    else:
        print(f"{list_of_queue.pop(0)} must wait")
    return tank_water


water_in_tank = int(input())

list_of_queue = []
start_filling = False

while True:
    current = input()

    if start_filling:
        if current == "End":
            break

        amount = [int(x) if x.isdigit() else x for x in current.split()]

        if amount[0] == 'refill':
            water_in_tank += amount[1]
        else:
            water_in_tank = check_water(amount[0], water_in_tank)
        continue

    if current == "Start":
        start_filling = True
        continue
    list_of_queue.append(current)

print(f"{water_in_tank} liters left")