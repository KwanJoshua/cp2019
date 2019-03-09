# Enter Input
num = int(input('Enter number: '))

# Function
def sum_series1(i):
    if i > 0:
        return (1/i) + sum_series1(i-1)
    else:
        return 0

# Main
print(sum_series1(num))
