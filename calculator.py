print("This is my calculator mini project")

while True:
    while True:
        try:
            a = float(input("input a first number: "))
            break
        except ValueError:
            print("INVALID INPUT / YOU MUST ENTER A NUMBER : ")

    while True:
        try:
            b = input("input a type of operations: ")
            if b in ("+","-","*","/"):
                break
            else:
                raise ValueError

        except ValueError:
            print("Please enter a type of an operator (+,-,*,/)")      

    while True: 
        try:
            c = float(input("input a first second: "))
            break
        except ValueError:
            print("INVALID INPUT / YOU MUST ENTER A NUMBER : ")


    if b == "+":
        result = (a + c)

    elif b == "-":
      result = (a - c)

    elif b == "/":
      result = (a / c)

    elif b == "*":
        result = (a * c)

    else:
       result = None

    if result != None:
        print("Your is ",result)   
    else:
        print("unxpected error")    

    repeat = input("Do you want to perform anthoer operation? (y/n): ")


    if repeat == "n":
        break

