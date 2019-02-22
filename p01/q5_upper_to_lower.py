# Enter Input
word = str(input('Enter Word: '))
w = []
s = []

# Changing into lowercase letter
for i in word:
    w.append(ord(i)+32)

for i in w:
    s.append(chr(i))

# Output
print(''.join(s))
