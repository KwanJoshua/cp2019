# Enter Input
num = int(input('Enter number: '))

# Function
def sum_series1(i):
    n = 1
    total = 0
    while n <= i:
        total += (1/n)
        n += 1
    print(total)

# Main
sum_series1(num)
