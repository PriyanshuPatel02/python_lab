def Fibonacci(N):
    if (N == 0):
        return 0
    elif (N == 1):
        return 1
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)
    
N = int(input("Enter the number\n"))
print("Fbonacci series is:\n")
for i in range(N):
    print(Fibonacci(i))
