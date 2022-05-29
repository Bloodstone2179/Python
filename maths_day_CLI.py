import random
#addition functions
def next():
    nextAdd()
def nextAdd():
    randomNum = random.randint(0,100)
    randomNum2 =random.randint(0,100) 
    print("1")
    print("What is " + str(randomNum) + " + " + str(randomNum2))
    ans = randomNum + randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        next()
def add():
    randomNum = random.randint(0,1000)
    randomNum2 =random.randint(0,1000) 
    print("1")
    print("What is " + str(randomNum) + " + " + str(randomNum2))
    ans = randomNum + randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextAdd()
    else:
        print("Wrong Try Again")
        nextAdd()

#subtraction functions
def nextSU():
    nextSub()
def nextSub():
    randomNum = random.randint(0,100)
    randomNum2 =random.randint(0,100) 
    print("1")
    print("What is " + str(randomNum) + " - "  + str(randomNum2))
    ans = randomNum - randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextSU()
def subtract():
    randomNum = random.randint(0,1000)
    randomNum2 =random.randint(0,1000) 
    print("1")
    print("What is " +  str(randomNum) + " - " + str(randomNum2))
    ans = randomNum - randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextSub()
    else:
        print("Wrong Try Again")
        nextSub()

#divide
def nextDIV():
    nextDivide()
def nextDivide():
    randomNum = random.randint(0,100)
    randomNum2 =random.randint(0,100) 
    print("1")
    print("What is " + str(randomNum) + " +/ " + str(randomNum2))
    ans = randomNum / randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextDIV()
def DIV():
    randomNum = random.randint(0,1000)
    randomNum2 =random.randint(0,1000) 
    print("1")
    print("What is " + str(randomNum) + " / " + str(randomNum2))
    ans = randomNum / randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextDIV()
    else:
        print("Wrong Try Again")
        nextDIV()
def nextMULTI():
    nextTimes()
def nextTimes():
    randomNum = random.randint(0,100)
    randomNum2 =random.randint(0,100) 
    print("1")
    print("What is " + str(randomNum) + " * " + str(randomNum2))
    ans = randomNum * randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextMULTI()
def MULTI():
    randomNum = random.randint(0,1000)
    randomNum2 =random.randint(0,1000) 
    print("1")
    print("What is " + str(randomNum) + " * " + str(randomNum2))
    ans = randomNum * randomNum2
    answer = int(input("What is your answer: "))
    if answer == ans:
        print("Well done heres another question")
        nextMULTI()
    else:
        print("Wrong Try Again")
        nextMULTI()


def sub():
    subtract()
def multi():
    MULTI()
def div():
    DIV()
print("Welcome to a maths Game")
print("\n")
print("\n")
print("Please pick 1-4:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
valid = bool(False)
op = str(input("OPTION: "))

while valid == False:
    if op == "1":
        add()
        valid = True
    elif op == "2":
        sub()
        valid = True
    elif op == "3":
        multi()
        valid = True
    elif op == "4":
        div()
        valid = True
    else:
        print("Input Invalid try again!!!!!")
        op = str(input("OPTION: "))