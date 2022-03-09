# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {student:random.randint(1, 100) for student in names}

# passed_students = {key:value for (key, value) in students_scores.items() if value > 51}
# print(passed_students)

# day 26 task 4
# with open("file1.txt") as file1:
#     numbers_1 = file1.readlines()
#     num_1 = [int(number.strip()) for number in numbers_1]
# with open("file2.txt") as file2:
#     numbers_2 = file2.readlines()
#     num_2 = [int(number.strip()) for number in numbers_2]

# result = [n for n in num_1 if n in num_2]

# print(result)

#Task 5

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
splited_sentence = sentence.split()

result = {sentence:len(sentence) for sentence in splited_sentence}

print(result)