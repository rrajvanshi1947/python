# print('Enter number of students in each class seperated by space.')

# studentList = list(map(int, input().split()))

studentList = list(map(int, input('Enter number of students in each class seperated by space.\n').split()))

def desksReq(students):
    desks = students/2 if students%2==0 else students//2 + 1
    return desks

desksList = list(map(desksReq, studentList))

print(desksList)
sum = 0
for item in desksList:
    sum += item

print(sum, 'is the number of desks required.') 

