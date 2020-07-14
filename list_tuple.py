def list_tuple(num):
    '''
    Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:

    34,67,55,33,12,98
    Then, the output should be:

    ['34', '67', '55', '33', '12', '98']
    ('34', '67', '55', '33', '12', '98')
    '''
    lst = []
    tpl = ()
    for i in num:
        lst.append(i)
        tpl.append(i)

val = input("Enter a sequence of numbers: ")
val.split(',')
lst = val.split(',')
tpl = tuple(lst) # convert list to tuple

print(lst)
print(tpl)

# alternative solutions
lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
                          # method name split. ',' inside split function does split where it finds any ','
                          # and save the input as list in lst variable

tpl = tuple(lst)          # tuple method converts list to tuple

print(lst)
print(tpl)

'''solution by: minnielahoti
'''
print(tuple(input("Enter a series of numbers separated by a comma :").split(',')))