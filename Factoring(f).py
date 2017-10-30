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
