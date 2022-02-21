from logo import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calc():
    print(logo)
    num1 = float(input("What's the first number? => "))

    for operator in operators:
        print(operator)

    calc_done = True
    while calc_done:
        operator_trigger = input("Pick an operation: => ")
        num2 = float(input("What's the next number? => "))
        calculator = operators[operator_trigger]
        answer = calculator(num1, num2)
        x = round(answer, 2)
        print(f"{num1} {operator_trigger} {num2} = {x}")

        u_i = input(f"Type 'y' to continue calculating with {x}, or type 'n' to start again. ")
        if u_i == 'y':
            num1 = answer
        else:
            calc_done = False
            calc()
        
calc()

# else:
    # operator_trigger = input("Pick an operation: => ")
    # num3= int(input("What's the next number? => "))
    # answer_two = calculator(answer_one, num3)
    # print(f"{answer_one} {operator_trigger} {num3} = {answer_two}")

# if operator_trigger == "+":
#     answer = operators[operator_trigger](num1, num2)
# elif operator_trigger == "-":
#     answer = operators[operator_trigger](num1, num2)
# elif operator_trigger == "*":
#     answer = operators[operator_trigger](num1, num2)
# elif operator_trigger == "/":
#     answer = operators[operator_trigger](num1, num2)
# else:
#     print("You must choose one of the operators.")