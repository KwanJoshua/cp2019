# Main
kg = 1

print('Kilograms', 'Pounds')
for i in range(9):
    pounds = kg*2.2
    pounds = '{0:.1f}'.format(pounds)
    print(kg, f'{pounds:^22}')
    kg += 1
for i in range (10,11):
    pounds = kg*2.2
    pounds = '{0:.1f}'.format(pounds)
    print(kg, f'{pounds:^20}')
