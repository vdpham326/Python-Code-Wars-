'''
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a 
single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''

def fact(num):
    factor = 1
    for i in range(1, num+1):
        factor = factor * i
    return factor
print(shortFact(n))

# alternative solutions
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(raw_input())
print fact(x)

n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)


print(fact(8))