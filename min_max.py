def Max_min(l1):
    min = 99999
    max = -1

    for item in l1:
        if min > item:
            min = item
        if max < item:
            max = item
    print('Minimum value is: ', min, '\nmaximum value is: ', max)

Arr = [1, 15, 8, 0, 9]
Max_min(Arr)
