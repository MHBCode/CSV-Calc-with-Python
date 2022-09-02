from random import random

num_stu  = int(50 * random())
students = num_stu if num_stu > 20 else num_stu + 25
num_grd  = int(5  * random())
grades   = num_grd if num_grd > 2 else num_grd + 3

csv_grades = open("grades.csv", "w")
csv_grades.write("StudentName")
for i in range(grades):
    csv_grades.write(",Grd_{}".format(i+1))
csv_grades.write("\n" )

for student in range(students):

    csv_grades.write("student_{:0>3d}".format(student+1))

    for i in range(grades):
        number = int(100 * random())
        if number < 60: number = 35 + number
        if 42 < number < 50: grade = 8 + number
        elif 70 < number < 85: grade = 10 + number
        else: grade = number

        csv_grades.write(",{:5d}".format(grade))
        #print(grade, end = ' ')

    csv_grades.write("\n")

print("\nnumber of students =", students)
print("\nnumber of grades =", grades,'\n')

csv_grades.close()

csv_grades = open("grades.csv")
print(csv_grades.read())
