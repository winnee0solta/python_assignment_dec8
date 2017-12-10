#author : Kishor Shrestha
#Define a global static password value by yourself. Then define a function which prompts user for a password. If the password is a match, print "password match" or else print "Wrong password"

mainPassword = 'password'

def askPassword():
    inputPassword = input("Enter the password !!!")
    if inputPassword == mainPassword:
        return True
    else:
        return False

if askPassword():
    print("Password matches !")
else:
    print("Password Doesnt mathches !!")