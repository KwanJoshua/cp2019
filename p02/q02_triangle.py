# Enter Input
s1 = int(input('Enter side 1: '))
s2 = int(input('Enter side 2: '))
s3 = int(input('Enter side 3: '))

# Main
if s1+s2 > s3 and s2+s3 > s1 and s1+s3 >s2:
    print(s1 + s2 + s3)
else:
    print('Invalid triangle!')
