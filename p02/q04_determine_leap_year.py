# Enter Input
year = int(input('Enter year: '))

# Main
if year%400 == 0 or (year%100 != 0 and year%4) == 0:
    print('Leap')
else:
    print('Non-Leap')
