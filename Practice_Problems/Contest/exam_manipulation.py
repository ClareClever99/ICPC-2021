initialinput = input().split(" ")
students = int(initialinput[0])
questions = int(initialinput[1])

tests = []

for i in range(students):
    tests.append(input())

grades = [1] * questions

for i in range(1, len(tests), 1):
    for j in range(questions):
        if tests[i][j] != tests[i-1][j]:
            grades[j] = 0

for grade in grades:
    if grade == 0:
        questions -= 1

print(questions)
