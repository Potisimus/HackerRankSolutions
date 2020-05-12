'''
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Input:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

Output:

Berry
Harry

'''


student_with_marks = []
marks = []
for i in range(int(input())):
    name = input()
    score = float(input())
    student_with_marks.append([name, score])
    marks.append(score)
marks = sorted(set(marks))
second_lowest_num = marks[1]


for i, j in sorted(student_with_marks):
    if j == second_lowest_num:
        print(i)

