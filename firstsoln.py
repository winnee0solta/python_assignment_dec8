#Define a function to determine whether the user's integer input is a even number or an odd number.

def checkevern(inValue = 0 ):
    if inValue % 2 == 0 :
        print("{} is even".format(inValue))
    else:
        print("{} is odd".format(inValue))

checkevern(int(input("Enter an integer value to find its odd or even")))