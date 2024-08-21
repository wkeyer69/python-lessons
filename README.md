# u create a game that asks u math questions and times it. 

import random 

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10

def problem_gen():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + operator + str(right)
    anwser = eval(expr)
    return expr, anwser



for i in range(total_problems):
    expr, anwser = problem_gen()
    while True:
        guess = input("problem number " + str(i + 1) + ": " + expr + " = ")
        if guess == str(anwser):
            break 


