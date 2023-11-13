
N=3
a=int(input('1st number: '))
b=int(input('2nd number: '))
e=int(input('3rd number: '))
def sort (c):
    for i in range(N-1):
       for j in range(N-1-i):
           if c[i] > c[i+1]:
                c[i], c[i+1] = c[i+1], c[i]
    return c
q=sort(a,b,e)
print (sort(q))