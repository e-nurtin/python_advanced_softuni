from _collections import deque

clothes_sequence = deque([int(x) for x in input().split()])
rack_capacity = int(input())

racks_needed = 1
current_rack = 0


while clothes_sequence:
    current_clothes = clothes_sequence.pop()
    
    if current_clothes + current_rack <= rack_capacity:
        current_rack += current_clothes
        continue

    racks_needed += 1
    current_rack = current_clothes

print(racks_needed)
