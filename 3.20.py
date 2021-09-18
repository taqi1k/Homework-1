# Taqi Syed
# 1863528

import math

wallHeight = int(input("Enter wall height (feet):\n"))
wallWidth = int(input("Enter wall width (feet):\n"))
area = wallHeight * wallWidth
print('Wall area:', area, 'square feet')

paintNeeded = area / 350
print('Paint needed: %.2f' % paintNeeded, 'gallons')
print('Cans needed:', math.ceil(paintNeeded), 'can(s)\n')

paintColors = {
    'red': 35,
    'blue': 25,
    'green': 23,
}
Color = input('Choose a color to paint the wall:\n')
print('Cost of purchasing', Color, 'paint:', '$' + str(paintColors[Color]))









