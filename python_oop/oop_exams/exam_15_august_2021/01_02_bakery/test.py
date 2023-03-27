from project.bakery import Bakery

bakery = Bakery("Elit")

print(bakery.add_food('Cake', 'Saher', 12))
print(bakery.add_food('Bread', 'Pitka', 2))
print(bakery.add_food('Bread', 'Iskender', 18))
print(bakery.add_drink('Water', "Soda Water", 200, 'Kinley'))
print(bakery.add_drink('Water', "Water", 500, 'Baldaran'))
print(bakery.add_drink('Tea', "Dark Tea", 180, 'Lipton'))
print(bakery.add_drink('Tea', "Chamonile Tea", 180, 'Lipton'))

print(bakery.add_table('InsideTable', 22, 6))
print(bakery.add_table('InsideTable', 2, 4))
print(bakery.add_table('InsideTable', 12, 10))
print(bakery.add_table('OutsideTable', 51, 5))
print(bakery.add_table('OutsideTable', 100, 5))


print(bakery.reserve_table(8))
print(bakery.reserve_table(10))
print(bakery.order_food(12, 'Saher', 'Pitka', 'Iskender'))
print(bakery.order_drink(12, 'Soda Water', 'Water', 'Dark Tea', 'Chamonile Tea'))
print(bakery.reserve_table(5))
print(bakery.reserve_table(5))
print(bakery.order_food(51, 'Saher'))
print(bakery.order_drink(51, 'Water'))
print(bakery.leave_table(12))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())
print(bakery.leave_table(51))
print(bakery.get_total_income())
print(bakery.get_free_tables_info())
