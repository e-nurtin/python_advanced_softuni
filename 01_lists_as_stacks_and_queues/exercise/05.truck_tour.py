## 2
from _collections import deque

gas_stations = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

copied_stations = gas_stations.copy()
index = 0
gas_in_tank = 0

while copied_stations:
	quantity, distance = copied_stations.popleft()
	
	gas_in_tank += quantity
	
	if gas_in_tank < distance:
		gas_stations.rotate(-1)
		copied_stations = gas_stations.copy()
		gas_in_tank = 0
		index += 1
		
	else:
		gas_in_tank -= distance
print(index)

#
#
## 1
#
# gas_stations = int(input())
#
# starting_station = 0
# gas_in_tank = 0
# stations_info = [input() for station in range(gas_stations)]
#
# station_found = False
# for station in range(gas_stations):
#     quantity, distance = [int(info) for info in stations_info[station].split()]
#
#     if quantity >= distance:
#         starting_station = station
#         station_found = True
#
#         for index in range(station, station + len(stations_info)):
#             if len(stations_info) <= index:
#                 index -= len(stations_info)
#
#             quantity, distance = [int(info) for info in stations_info[index].split()]
#             gas_in_tank += quantity
#
#             if gas_in_tank >= distance:
#                 gas_in_tank -= distance
#             else:
#                 gas_in_tank = 0
#                 station_found = False
#                 break
#
#     if station_found:
#         print(starting_station)
#         break
#
#
