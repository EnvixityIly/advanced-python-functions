number = [1,2,3,4,5,6]
even = [x for  x in number if x%2==0]
print(even)

n1 = [1,2,3]
n2 = [2,3,4]
n3 = [5,6,7]

nSum = map(lambda x,y,z: x+y+z, n1,n2,n3)

print(list(nSum))

def sq(n):
    return n*n
num = [5,4,3,4,5,8,930,2]

res = map(sq, num)
print(list(res))