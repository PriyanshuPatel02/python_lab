def Is_Palindrome(n):
    reversed_num = 0
    while(n != 0):
        last_degit = n%10
        reversed_num = (reversed_num*10) + last_degit
        n = n//10
    
    if reversed_num == n:
        return 1
    else:
        return 0

n = int(input("Enter"))
Is_Palindrome(n)

if Is_Palindrome(n):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")