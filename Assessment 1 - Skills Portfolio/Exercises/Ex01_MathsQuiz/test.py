import random as rd

randomIntEasy1 = rd.randint(1,9)
randomIntEasy2 = rd.randint(1,9)
randomOperator = rd.choice(('+', '-'))

def calculate():
    if randomOperator == '+':
        sum = (randomIntEasy1 + randomIntEasy2) 
        print(f"{randomIntEasy1} + {randomIntEasy2} = {sum}")

calculate()