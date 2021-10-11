import sys

user_input = float(input('Enter a value: '))
num_to, num_from = 0, 0

units = ('mm', 'cm', 'm', 'km', 'inches', 'ft', 'yds', 'miles')
conversions = (1, 10, 1000, 1e6, 25.4, 304.8, 914.4, 1.609344e6)

unit_from = input(f'Convert from {units}: ')
unit_to = input('Convert to: ')

if unit_from not in units or unit_to not in units:
    print(f'Invalid unit. Please use available units {units}.')
    sys.exit(1)

for i in range(0, len(units)):
    if units[i] == unit_from:
        num_from = user_input * conversions[i]

for j in range(0, len(units)):
    if units[j] == unit_to:
        num_to = num_from / conversions[j]

print(f'Output: {round(user_input, 2)} {unit_from} is equal to {round(num_to, 2)} {unit_to}')
