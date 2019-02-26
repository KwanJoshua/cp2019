# Enter Input
n = int(input('Enter number: '))

# Main
i = 1
n1 = n
factor = []
while (0 < i <= n):
    if n1 % i == 0:
        factor.append(i)
        i += 1
    else:
        i += 1

print(','.join(map(str, factor)))
