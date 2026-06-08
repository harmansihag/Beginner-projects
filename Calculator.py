#Calculator with +-%/*//** operations
num1= float(input("First number :"))
num2 = float(input("Second number :"))
operator = str(input("Enter the operation:"))

if operator != "+" and operator != "-" and operator != "*" and operator != "**" and operator != "/" and operator != "//" and operator != "%" : 
    print("INVALID OPERATOR") 
elif operator == "+" : 
    result = num1 + num2
elif operator == "-" : 
    result = num1 - num2
elif operator == "*" : 
    result = num1*num2
elif operator == "**" :  # num1 to the power num2
    result = num1**num2
elif operator == "/" : 
    result = num1 / num2
elif operator == "//" : # Round off the quotient
    result = num1 // num2
elif operator == "%" : # gives the remainder 
    result = num1 % num2
print(round(result, 4))
