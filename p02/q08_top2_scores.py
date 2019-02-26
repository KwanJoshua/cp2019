# Enter Input
number = int(input('Enter number of students: '))
name = []
score = []
for i in range (0,number):
    name.append(input('Enter name of student: '))
    score.append(int(input('Enter score of student: ')))

# Main
score_1 = sorted(score)
highest = score_1[-1]
second_highest = score_1[-2]

print('Student with the highest score is',\
      name[score.index(highest)], 'with a score of', highest)
print('Student with the second highest score is',\
      name[score.index(second_highest)], 'with a score of',\
      second_highest)
