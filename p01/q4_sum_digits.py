# Enter Input
number= int(input('Enter Number: '))

# Calculation
digits = 0
while (number > 10):
    digits+=number%10
    number = number//10
digits+=number

# Output
print('Sum of digits: ', digits)
