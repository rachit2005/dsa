def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


def factorial_series(show=True):
    n = int(input("enter the number"))
    fac_sereis = []
    for i in range(n+1):
        res = factorial(i)
        fac_sereis.append(res)
        if show:
            print(res)

    print(fac_sereis)

# factorial_series(show=False)

'''***************************** Fibonnaci *******************************'''

def fibonnaci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
def fibonnaci_ser(show=True):
    n = int(input("enter number: "))
    fibonnaci_series = []
    for i in range(n+1):
        fibonnaci_series.append(fibonnaci(i))
        if show:
            print(fibonnaci(i))

    print(fibonnaci_series)

fibonnaci_ser()
