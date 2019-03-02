# Enter Input
num = int(input('Enter number: '))

# Function
def convert_ms(n):
    time = []
    h = n//3600000
    m = n//60000
    s = n//1000
    time.append(h)
    time.append(':')
    time.append(m - h*60)
    time.append(':')
    time.append(s - m*60)
    for i in time:
        print(i, end = '')
convert_ms(num)
