print("My module is running")

def fromcelcius():
    usertemp = input("Enter the temp you want converted to degrees fahrenheit: ")
    temp = float(usertemp)
    print(type(temp))
    return((temp *1.8) + 32)

def fromfahrenheit(value):
    return(value-32) / 1.8
    