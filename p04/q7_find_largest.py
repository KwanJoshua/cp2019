# Enter list
length = int(input('Enter length of list: '))
alist = []
for i in range (length):
    alist.append(int(input('Enter number: ')))

# Funtion
def find_largest(n):
    if len(n) > 0:
        if n[0] > find_largest(n[1:]):
            return n[0]
        else:
            return find_largest(n[1:])
    else:
        return 0
# Main
print(find_largest(alist))
