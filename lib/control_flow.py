#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username=="ADMIN" or username=="admin") and (password=='12345'):
        return 'Access Granted'
    else:
        return "Access Denied"



def hows_the_weather(temperature):
    # your code here
    if (temperature<40):
        return "It's brisk out there!"
    elif (temperature < 65 and temperature >39):
        return "It's a little chilly out there!"
    elif (temperature >85):
        return  "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
