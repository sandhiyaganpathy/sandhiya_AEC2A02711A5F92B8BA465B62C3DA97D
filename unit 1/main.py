#python program to find the factorial of a number using recursion 
#fact_recur.py
def fact(m):
  if m<=1:
    return 1
  else:
    return m*fact(m-1)
#Main program 
n=int(input("Enter the value of n:"))
print("the factorial of",n,"is",fact(n))
