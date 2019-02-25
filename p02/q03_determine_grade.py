# Enter Input
grade = int(input('Enter Score: '))

# Main
if 70 <= grade <= 100:
    print('A')
elif 60<= grade < 70:
    print('B')
elif 55 <= grade < 60:
    print('C')
elif 50 <= grade < 55:
    print('D')
elif 45 <= grade < 45:
    print('E')
elif 35 <= grade < 45:
    print('S')
elif 0 <= grade < 35:
    print('U')
else:
    print('Invalid! Score must be within 0 - 100.')
