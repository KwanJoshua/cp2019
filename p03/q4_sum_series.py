# Enter Input
num = int(input('Enter number: '))

# Function
def m_series(i):
    s = 0
    a = 1
    while a <= i:
        s += (a/(a+1))
        a += 1
    print(('{0:.3f}'.format(s)))

m_series(num)

# Test Program (table)
def m_table(n):
    a = 1
    b = 0
    print('i', f"{'m(i)':^16}")
    while a <= n:
        if len(str(a)) == 1:
            b += (a/(a+1))
            c = ('{0:.4f}'.format(b))
            print(a, f'{c:^16}')
            a += 1
        elif len(str(a)) == 2:
            b += (a/(a+1))
            c = ('{0:.4f}'.format(b))
            print(a, f'{c:^14}')
            a += 1

m_table(20)
