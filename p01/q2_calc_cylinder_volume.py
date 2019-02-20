# Enter Input
radius = float(input('Radius (m): '))
length = float(input('Length (m): '))

# Calculation
from math import pi
area = 2*radius**2*pi + 2*pi*radius*length
volume = radius**2*length*pi

# Output
print('Area (m^2): ', area)
print('Volume (m^3): ', volume)
