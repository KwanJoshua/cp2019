# Enter Input
num = int(input('Enter number: '))

# Function
def sum_series2(i):
    n = 1
    total = 0
    while n <= i:
        total += (n/(2*n + 1))
        n += 1
    print(total)

# Main
sum_series2(num)
