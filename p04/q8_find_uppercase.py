# Enter Word
word = input('Enter word: ')

# Funtion
def find_num_uppercase(str):
    total = 0
    if len(str) > 0:
        if 64 < ord(str[0]) < 91:
            return 1 + find_num_uppercase(str[1:])
        else:
            return find_num_uppercase(str[1:])
    else: return 0

# Main
print(find_num_uppercase(word))
