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
