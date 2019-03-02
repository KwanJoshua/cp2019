# Enter Input
num = int(input('Enter number: '))

# Function
i = 0
def reverse_int(n):
    reverse = 0
    while (i < n):
        reverse = reverse*10 + n % 10
        n = n//10
    print(reverse)
        
reverse_int(num)
