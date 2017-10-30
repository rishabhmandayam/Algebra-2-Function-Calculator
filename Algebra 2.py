import math
print(math.sqrt(25))
print("""
        Not Texas Instruments Calculator IT 100
        Algebra function calculator
""")
start = input("""
        Press 's' to begin
""")
if start == "s":
    print("Opening Calculator function list...")
    while True:
        print("Choose a function by typing the letter in ().")
        print("""
Quadratic formula:(q)
Factoring/Expanding:(f)
Plain old arithmitic:(a)
Degree to Radian:(DR)
Radian to Degree:(RD)
""")
        x = input(": ")
        if x == "q":
            print("""
ax2 + bx + c
""")
            a = int(input("a:"))
            b = int(input("b:"))
            c = int(input("c:"))
            work = b*-1
            morework = b*b
            nonethelesswork = 4*a*c
            actuallyimportantstuff = morework - nonethelesswork
            almost_done = math.sqrt(actuallyimportantstuff)
            answer1part1 = work+almost_done
            answer1part2 = answer1part1/(2*a)
            answer2part1=work-almost_done
            answer2part2=answer2part1/(2*a)
            print("x = {"+str(answer1part2)+", "+str(answer2part2)+"}")
        elif x == "f":
            print("Choose your factoring/expanding form:")
            print("""
a squared - b squared(1)
(a+b) squared(2)
(a-b) squared(3)
a cubed - b cubed(4)
a cubed + b cubed(5)
""")
            factoring = input(": ")
            if factoring == "1":
                print("a2 - b2")
                a = int(input("a2:"))
                b = int(input("b2:"))
                answer= ("(" + str(math.sqrt(a))+" + " + str(math.sqrt(b)) + ")("+ str(math.sqrt(a))+" - " + str(math.sqrt(b)) + ")")
                print(answer)
            elif factoring == "2":
                print("(a+b)squared")
                a = int(input("a:"))
                b = int(input("b:"))
                answer = (str(math.pow(a, 2)) + " + " + str(a*b*2) + " + "+ str(math.pow(b, 2)))
                print(answer)
            elif factoring == "3":
                print("(a-b)squared")
                a = int(input("a:"))
                b = int(input("b:"))
                answer = (str(math.pow(a, 2)) + " - " + str(a*b*2) + " + "+ str(math.pow(b, 2)))
                print(answer)
            elif factoring == "4":
                a = int(input("a:"))
                b = int(input("b:"))
                answer = ("("+ str(a) + " - " + str(b) + ")(" + str(math.pow(a, 2)) + " + " + str (a*b) + " + " +str(math.pow(b, 2))+ ")")
                print(answer)
            elif factoring == "5":
                a = int(input("a:"))
                b = int(input("b:"))
                answer = ("("+ str(a) + " + " + str(b) + ")(" + str(math.pow(a, 2)) + " - " + str (a*b) + " + " +str(math.pow(b, 2))+ ")")
                print(answer)
        
        elif x == "a":
            operation=input("Which operation?(+,-,x,/): ")
            if operation == "+":
                a=input("enter number 1")
                b=input("emter number 2")
                answer=(int(a)+int(b))
                print(str(answer))
            elif operation == "-":
                a=input("enter number 1")
                b=input("emter number 2")
                answer=(int(a)-int(b))
                print(str(answer))
            elif operation == "x":
                a=input("enter number 1")
                b=input("emter number 2")
                answer=(int(a)*int(b))
                print(str(answer))
            elif operation == "/":
                a=input("enter number 1")
                b=input("emter number 2")
                answer=(int(a)/int(b))
                print(str(answer))
            else:
                print("ERROR:Value outside operation library")
        elif x == "DR":
            degree=input("Enter your value in degrees(don't enter pi): ")
            radian=int(degree)/180
            print(str(radian)+" pi radians")
        elif x == "RD":
            radian=input("Enter your value in radians(don't enter pi): ")
            degree=int(radian)*180
            print(str(degree)+"""
--- radians
pi
""")
        elif x=="9":
            print("Welcome to the Error Library")
            error_type=input("Enter the error number: ")
            if error_type=="6823":
                print("'s' not typed")
            else:
                print("The number you have typed is not an error recorded in this library. Please check if you typed it in correctly")

        else:
          print("ERROR: Value outside function library")  
else:
    print("ERROR: Error 6823. To look up error, type '9' when choosing a function, then enter the error #.")

