# Enter list
length = int(input('Enter length of list: '))
alist = []
for i in range (length):
    alist.append(input('Enter number: '))

# Funtion
def find_largest(n):
    n.sort()
    print(n[-1])

# Main
find_largest(alist)
