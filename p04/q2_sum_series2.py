# Enter Input
num = int(input('Enter number: '))

# Function
def sum_series2(i):
    if i > 0:
        return (i / (2*i + 1)) + sum_series2(i-1)
    else:
        return 0

# Main
print(sum_series2(num))
