#addition
a = 3 + 5

#subtraction 
b = 7 - 4

#multiply #always come first
c = 3 * 3

#division always come first
d = 5 / 2 #always return float type

#square
e = 2 ** 3 #superscript

#moduo


#PEMDAS principle LR(lef to right)
"""
1. Parentheses ()
2. Exponents **
3. Multiplication * LR(lef to right) principle
4. Division / LR(lef to right) principle
5. Addition + 
6. Subtraction - 
"""

print(3 * 3 + 3 / 3 - 3) # = 7
print(3 * (3 + 3) / 3 - (3)) #3

#task 2 for day 2

# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26

height = float(input("enter your height: "))
weight = float(input("enter your weight: "))

result = int(weight / (height * height))
print(result)