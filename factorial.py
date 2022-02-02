def Factorial(N):
    if (N == 0) or (N == 1):
        return 1
    else:
        return N*Factorial(N-1)


N = int(input("Enter the number\n"))
print(Factorial(N))
