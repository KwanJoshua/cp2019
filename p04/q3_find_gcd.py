# Enter Input
num_1 = int(input('Enter number: '))
num_2 = int(input('Enter number: '))

# Funtion
def gcd(m, n):
    if m % n == 0:
        print(n)
    else:
        gcd(n, m % n)

# Main
gcd(num_1, num_2)
