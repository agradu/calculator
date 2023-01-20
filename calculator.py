# setings
import sys
import random
joke_list = ["Keep learning! Next time, maybe don't ask me that.","Great man! Any Kid knows that.","Bah... It's gonna be boring!","Realy? This is what you ask me?","No, somoane help me!"]

if len(sys.argv) == 4: # Calculator - argument mode
    print ("Simple calculator - argument mode")
    n1 = int(sys.argv[1])
    calc = sys.argv[2]
    n2 = int(sys.argv[3])
    if calc == "+":
        result = n1 + n2
    elif calc == "-":
        result = n1 - n2
    elif calc == 'x':
        result = n1 * n2
    elif calc == "/":
        result = n1 / n2
    else:
        result=""
    if result != "":
        print("Result:",result)
    else:
        print("Hey! Did you try to cheat me?")
        print("The arguments must be like: nuber1(0,1,2...) operand(+-x/) nuber2(0,1,2...).")
    print(joke_list[random.randrange(0,4)])

else: # Calculator - input mode
    print ("Simple calculator - input mode")
    n1 = int(input("First number: "))
    calc = input("Operand: ")
    n2 = int(input("Last number: "))
    if calc == "+":
        result = n1 + n2
    elif calc == "-":
        result = n1 - n2
    elif calc == '*':
        result = n1 * n2
    elif calc == "/":
        result = n1 / n2
    else:
        result=""
    if result != "":
        print("Result:",result)
    else:
        print("Hey! Did you try to cheat me?")
    print(joke_list[random.randrange(0,4)])