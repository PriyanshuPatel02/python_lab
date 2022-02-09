def Fibonacci(N):
    if (N <= 1):
        return N
    
    else:
        return Fibonacci(N-1) + Fibonacci(N-2)

N = int(input("Enter the number\n"))
print("Fbonacci series is:")

for i in range(N):
    print(Fibonacci(i))

# fibonacci sequence is 
# 0 1 1 2 3 5 8 