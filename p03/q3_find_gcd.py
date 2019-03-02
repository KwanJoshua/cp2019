# Enter Input
num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

# Function
def gcd(m, n):
    cd = []
    a = 1
    b = 1
    i = 1

    while i <= (m):
        if m % i == 0:
            cd.append(i)
            i += 1
        else:
            i += 1
    
    while a <= (n):
        if n % a == 0:
            cd.append(a)
            a += 1
        else:
            a += 1

    cd.sort()
    while b <= len(cd):
        if cd[-b] == cd[-(b+1)]:
            print('GCD =',cd[-b])
            break
        else:
            b+=1

gcd(num_1, num_2)

# Test Program
gcd(24, 16)
gcd(255, 25)
