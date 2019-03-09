# Enter Input
word = input('Enter word: ')
letter = input('Enter letter: ')

# Funtion
def count_letter(str, ch):
    if len(str) > 0:
        if str[0] == ch:
            return 1 + count_letter(str[1:], ch)
        else:
            return count_letter(str[1:], ch)
    else:
        return 0

# Main
print(count_letter(word, letter))
