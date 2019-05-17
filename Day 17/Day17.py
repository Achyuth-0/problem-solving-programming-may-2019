def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n-1)*n

def sumN(n):
    if n == 1:
        return 1
    return numN(n-1)+n