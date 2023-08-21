from math import sqrt
with open("greet.txt") as greet:
    print(greet.read())

isExit = choose = firstNum = secondNum = 0

while(not isExit):
    choose = 0
    print("Choose your operation:\n1)\t+\n2)\t-\n3)\t/\n4)\t*\n5)\t%\n6)\tsqrt(x)\t\n7)\t% of")
    choose = int(input("\t\t\t"))

    if(choose < 1 or choose > 7):
        print("Error! Try again.\n")
        continue

    print("Enter first number: ")
    firstNum = int(input("\t\t\t"))    

    if(choose != 6):
        print("Enter second number: ")
        secondNum = int(input("\t\t\t"))

    if(choose == 1):
        print(f"Your result is {firstNum} + {secondNum} = {firstNum + secondNum}")
    
    elif(choose == 2):
        print(f"Your result is {firstNum} - {secondNum} = {firstNum - secondNum}")

    elif(choose == 3):
        print(f"Your result is {firstNum} / {secondNum} = {firstNum / secondNum}")

    elif(choose == 4):
        print(f"Your result is {firstNum} * {secondNum} = {firstNum * secondNum}")

    elif(choose == 5):
        print(f"Your result is {firstNum} % {secondNum} = {int(float(firstNum) % secondNum)}")

    elif(choose == 6):
        print(f"Your result is sqrt({firstNum}) =", sqrt(firstNum))

    elif(choose == 7):
        print(f"Your result {secondNum}% of {firstNum} =", firstNum*(secondNum/100))

    print("\nWant to continue? (y/n)")
    choose = str(input())

    if(choose == "y" or choose == "yes"):
        isExit = 0
    else:
        isExit = 1