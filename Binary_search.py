def Binary_search(l1, value):
    s = 0
    e = len(l1)-1
    mid = (s+e)//2

    while(s <= e):
        if l1[mid] == value:
            return 1

        elif value < l1[mid]:
            e = mid - 1

        else:
            s = mid + 1

        mid = (s + e)//2


l1 = [1, 2, 3, 4, 5, 6, 7, 8]

if(Binary_search(l1, 9)):
    print("present")

else:
    print("not present")
