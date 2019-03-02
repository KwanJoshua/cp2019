# Enter Input
num = int(input('Enter number: '))

# Function
def print_matrix(n):
    import random
    a = 0
    i = 0
    matrix = []
    while i < (n**2):
        matrix.append(random.randint(0, 1))
        i += 1
    while a < (n**2):
        for b in matrix[a:a+n]:
            print(b, end = ' ')
        a += n
        print('')

print_matrix(num)
