def Fib(n):
    if n == 1:
        return 1 # returns value of 1.
    if n == 0:
        return 0
    # Fibbonacci
    else: 
        return Fib(n-1) + Fib(n-2)
print(Fib(7))