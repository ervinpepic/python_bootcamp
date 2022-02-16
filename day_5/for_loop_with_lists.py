fruits = ["Apple", "Peach", "Pear"]
for fr in fruits:
    print(f"Your fruits is: {fr}")
    print(fr + " Pie")

# Day 5 task 1:

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

height_sum = 0
number_of_students = 0
result = 0

for i in student_heights:
    number_of_students += 1

for n in student_heights:
    height_sum += n
    result = height_sum / number_of_students

# print(round(result))

# Day 5 task 2:
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

current = 0
a = 0
b = 0

for i in student_scores:
    current = i
    if current > a:
        a = current
        b = a
print(f"The highest score in the class is: {b}")