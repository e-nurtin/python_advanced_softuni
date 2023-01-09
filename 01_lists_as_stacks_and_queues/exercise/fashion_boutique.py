clothes_sequence = [int(x) for x in input().split()]
rack_capacity = int(input())

racks_needed = 1
current_rack = 0

ordered_clothes = clothes_sequence[-1::-1]


for value in ordered_clothes:

    if value + current_rack <= rack_capacity:
        current_rack += value
        continue

    racks_needed += 1
    current_rack = value

print(racks_needed)

