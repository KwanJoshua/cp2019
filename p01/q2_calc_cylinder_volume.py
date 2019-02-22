# Enter Input
radius = float(input('Radius (m): '))
length = float(input('Length (m): '))

# Calculation
from math import pi
volume = radius**2*length*pi

# Output
print('Volume (m^3): ', volume)
