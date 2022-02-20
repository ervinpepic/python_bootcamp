programming_dict = {
    "bug": "An error in an program that prevents the program for running as expected",
    "function": "A piece of code that can easily call over and over again",
}
#retireve items from the dict
print(programming_dict["bug"])

programming_dict["loop"] = "The action ov doing something over and over"
print(programming_dict)

empty_dict = {}

#wipe an existing dict
# programming_dict = {}

#edit an item in the dict

programming_dict["bug"] = "error in the software"
print(programming_dict)

#loop over an dict

for key, value in programming_dict.items():
    print(f"Key: {key} => value: {value}")

#or
for key in programming_dict:
    print(key, programming_dict[key])

# Day 9 task 1:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for score in student_scores:
    x = student_scores[score]
    if x >=91 and x <=100:
        student_grades[score] = "Outstanding"
    elif x >=81 and x <=90:
        student_grades[score] = "Exceeds Expectations"
    elif x >=71 and x <=80:
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)