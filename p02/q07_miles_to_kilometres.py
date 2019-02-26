# Main
print('Miles', 'Kilometers', 'Kilometres', 'Miles')
miles = 1
km_1 = 20
for i in range (9):
    km = miles*1.609
    km = '{0:.3f}'.format(km)
    miles_1 = km_1/1.609
    miles_1 = '{0:.3f}'.format(miles_1)
    print(miles, f'{km:^18}', km_1, f'{miles_1:^14}')
    miles += 1
    km_1 += 5
    
for i in range (10,11):
    km = miles*1.609
    km = '{0:.3f}'.format(km)
    miles_1 = km_1/1.609
    miles_1 = '{0:.3f}'.format(miles_1)
    print(miles, f'{km:^16}', f'{km_1:^4}', f'{miles_1:^12}')
