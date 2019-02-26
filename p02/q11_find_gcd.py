# Enter Input
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number '))

# Main
if n1 < n2:
    i = n2
    while (0 < i <= n2):
        if n2 % i == 0 and n1 % i == 0:
            print('Greatest common divisor is', i)
            break
        else:
            i -= 1
else:
    i = n1
    while (0 < i <= n1):
        if n1 % i == 0 and n2 % i == 0:
            print('Greatest common divisor is', i)
            break
        else:
            i -= 1
