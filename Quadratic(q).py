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
