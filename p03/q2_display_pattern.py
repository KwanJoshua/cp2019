# Enter Input
num = int(input('Enter number: '))

# Function
def display_pattern(n):
    pattern = []
    for i in range (1, n+1):
        pattern.insert(0, i)
        print('{:>20}'.format(' '.join(map(str, pattern))))

display_pattern(num)
