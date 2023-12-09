def Factorial(n):
    #This is so nothing is equated to 0...
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1) 
#With 10, it's essentially 10 * (10-1) * (9-1) * (8-1) and so on...
    
print(Factorial(10)) #Replace 10 with any other number.