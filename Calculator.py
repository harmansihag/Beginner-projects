#Calculator with +-%/*//** operations
num1= float(input("First number :"))
num2 = float(input("Second number :"))
operator = str(input("Enter the operation:"))
oplist= [ "+" , "-" , "*" , "**", "/" , "//" , "%"]

if operator not in oplist : 
    print("INVALID OPERATOR") 
    exit() # ends the program so the print at last isnt triggered
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
print(f"{num1} {operator} {num2} = {round(result, 4)}") 
