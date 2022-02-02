def Is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            return True

n = int(input("Enter the number\n"))

if Is_prime(n):
    print("Number is prime")

else:
    print("Number is not prime ")
