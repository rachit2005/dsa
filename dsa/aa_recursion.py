# calling a function in the function itself

def factorial(num):
    if num ==0 or num ==1:
        return 1
    return num*factorial(num - 1)

print(factorial(4))

# make fibonacci sequence

# f(n) = f(n-1) + f(n-2) 

def fibonaci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonaci(number-1) + fibonaci(number-2)

print(fibonaci(9)) #34
