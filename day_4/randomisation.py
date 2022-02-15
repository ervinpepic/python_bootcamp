import random
# import module_1
# x = random.randint(1, 99)
# print(x)
# print(module_1.pi)

# # random float

# ran_float = random.random()
# print(ran_float * 5)

# ls = random.randint(1, 100)
# print(f"Your ls is {ls}")

# Day 4 task 1 Head or Tail

# head_tail = random.randint(0,1)
# if head_tail == 1:
#     print("Heads")
# else:
#     print('Tails')

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
x = random.randint(0,1)
if x == 1:
    print("Heads")
else:
    print('Tails')