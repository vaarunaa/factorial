def factorial(n):
  if n==0 or n==1:
    retuirn 1
  else:
    return n*factorial(n-1)
num=int(input("enter a number:"))
print(f"Factorial of{num} is {factorial(num)}")
    
