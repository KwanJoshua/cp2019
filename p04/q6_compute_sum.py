# Enter Input
num = int(input('Enter number: '))

# Function
def sum_digits(n):
    if n > 0:
        return n%10 + sum_digits(n//10)
    else:
        return 0

# Main
print(sum_digits(num))
