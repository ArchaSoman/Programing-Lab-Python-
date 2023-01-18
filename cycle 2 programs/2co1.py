# Python program to find the factorial of a number provided by the user.
"""num = int(input("Enter a number: "))
factorial=1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)"""
   
def calc_factorial(x):
    if x == 1:
        return 1;
    else:
            return (x * calc_factorial(x-1))
num=int(input("enter a no"))
print("the factorial is",num,"is",calc_factorial(num))