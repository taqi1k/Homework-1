# Taqi Syed
# 1863528

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

print('Select first service:')
service1 = input()
print('Select second service:\n')
service2 = input()

print("Davy's auto shop invoice\n")
total_price = 0
if service1 == 'Oil change':
    print('Service 1: Oil change, $35')
    total = total_price + 35
elif service1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    total = total_price + 19
elif service1 == 'Car wash':
    print('Service 1: Car wash, $7')
    total = total_price + 7
elif service1 == 'Car wax':
    print('Service 1: Car wax, $12')
    total = total_price + 12
elif service1 == '-':
    print('Service 1: No service')
    total = total_price + 0
else:
    print('Service 1: Invalid option')


if service2 == 'Oil change':
    print('Service 2: Oil change, $35')
    total = total_price + 35
elif service2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total = total_price + 19
elif service2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total = total_price + 7
elif service2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total = total_price + 12
elif service2 == '-':
    print('Service 2: No service')
    total = total_price + 0
else:
    print('Service 2: Invalid option')

print('\n')

print('Total: ${}'.format(total_price))







