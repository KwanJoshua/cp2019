# Enter Input
num = int(input('Enter number: '))

# Funtion
def reverse_int(n):
    if n > 0:
        print(n % 10, end='')
        reverse_int(n // 10)
    elif n == 0:
        print('')
            
# Main
reverse_int(num)
