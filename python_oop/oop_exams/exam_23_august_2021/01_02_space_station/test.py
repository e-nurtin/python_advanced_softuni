from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut('Biologist', 'Mark'))
print(space_station.add_astronaut('Biologist', 'Greta'))
print(space_station.add_astronaut('Geodesist', 'Phillip'))
print(space_station.add_astronaut('Geodesist', 'Paul'))
print(space_station.add_astronaut('Meteorologist', 'Pat'))
# print(space_station.add_astronaut('Meteorologist', 'Daniel'))
# print(space_station.add_astronaut('Meteorologist', 'Neil'))

print(space_station.add_planet('OM-3322-Ms', "rock, shiny material, geode, Onyx, Cheese, lollipop, ice, mithril, bread"))
print(space_station.add_planet('SD-0092-Mt', "rock, shiny material, geode, goo, poo, animal, mooo, alo"))
print(space_station.add_planet('Earth', "two, more, items, digital device, tree, plant, water, lal, pal, kal, sal, too many items, some, moore, itemss, yess, now its ok"))
# print(space_station.add_planet('Mars', "digital device, tree, plant, water, lal, pal, kal, sal, too many items"))


print(space_station.retire_astronaut('Pat'))

print(space_station.send_on_mission('OM-3322-Ms'))
# space_station.recharge_oxygen()
print(space_station.send_on_mission('Earth'))
print(space_station.send_on_mission('SD-0092-Mt'))
# print(space_station.send_on_mission('Mars'))

print(space_station.report())