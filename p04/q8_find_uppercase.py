# Enter Word
word = input('Enter word: ')

# Funtion
def find_num_uppercase(str):
    total = 0
    i = 0
    while i <len(str):
        if 64 < ord(str[i]) < 91:
            total += 1
            i += 1
        else:
            i += 1
    print(total)

# Main
find_num_uppercase(word)
