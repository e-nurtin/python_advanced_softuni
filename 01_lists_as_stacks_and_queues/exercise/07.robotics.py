import datetime


def change_time(time):
    time = time + datetime.timedelta(seconds=1)
    return time


robots = [[int(y) if y.isdigit() else y for y in x.split('-')] for x in input().split(';')]
hour, minutes, seconds = (int(x) for x in input().split(':'))
tm = datetime.datetime(100, 1, 1, hour, minutes, seconds)

current_cycle_robots = [robot.copy() for robot in robots]

current_robot = ''
items_to_process = []

while True:
    command = input()
    if command == 'End':
        break
    items_to_process.append(command)

for robot in robots:
    tm = change_time(tm)
    current_time = tm.time()
    if items_to_process:
        print(f"{robot[0]} - {items_to_process.pop(0)} [{current_time}]")


while len(items_to_process) > 0:
    tm = change_time(tm)
    current_time = tm.time()
    current_item = items_to_process.pop(0)

    for robot in range(len(robots)):
        current_cycle_robots[robot][1] -= 1
        if current_cycle_robots[robot][1] == 0:
            current_robot = current_cycle_robots[robot][0]
            current_cycle_robots[robot] = robots[robot].copy()
            break

    if current_robot:
        print(f"{current_robot} - {current_item} [{current_time}]")
        current_robot = ''
    else:
        items_to_process.append(current_item)

