
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
▼
## ********Day 54 Start**********
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2
  
def subtract(n1, n2):
    return n1 - n2
  
def multiply(n1, n2):
    return n1 * n2
  
def divide(n1, n2):
    return n1 / n2
  
##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)
  
result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")
    
    def nested_function():
        print("I'm inner")
      
    nested_function()
  
outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")
    
    def nested_function():
        print("I'm inner")
      
    return nested_function
  
inner_function = outer_function()
inner_function


## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function
  
@delay_decorator
def say_hello():
    print("Hello")
  
#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")
  
#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()