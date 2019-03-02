# Function
def is_prime(n):
    if n <= 1:
        return False
    else:
        factors = []
        for i in range (1, n+1):
            if n % i ==0:
                factors.append(i)
        if len(factors) == 2:
            return True
        else:
            return False

# Test Program
prime_no = []
a = 0
i = 1
while len(prime_no) < 1000:
    if is_prime(i) == True:
        prime_no.append(i)
        i += 1
    else:
        i += 1
while a < 1000:
    for b in prime_no[a:a+10]:
        print(b, end = ' ')
    a += 10
    print('')
