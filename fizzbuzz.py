# Creating a program to print numbers from 1 to 50 
# Numbers which arefactor of 3 will display fizz in front of them,
# and NUmbers which are factors of 5 will display buzz in front of them, 
# and the factors of both will display fizzbuzz


for num in range (1, 51): 
    if (num % 3 != 0 and num % 5 != 0): # prints all non 3 and 5 factor nums 
        print(num)
    else: 
        pass
    if ( num % 3 == 0 and num % 5 ==0 ): # condn which will have nested fizz and buzz 
        print(num , "Fizzbuzz")
    else : 
        pass 
        if ( num % 3 == 0 ):
            print(num , "fizz")
        elif ( num % 5 == 0 ): 
           print(num , "buzz")

