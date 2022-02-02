f = open('sample.txt', 'r')

data = f.readlines()
count = 0
count_ele = 0
for lines in data:
    print(lines)
    count += 1
    for element in lines:
        count_ele += 1

print('Total number of element is:', count_ele)
print("Total number of lines is:", count)
f.close()
