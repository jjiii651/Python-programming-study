# A,B = map(int,input().split(' '))

# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

# score = [80,90,100,'hi']
# print(score[0:3])

# a= 'hellp'
# print(len(a)) #갯수

# a = [1,3,4,5,6,7]
# b = [35.4,6,4,5,3,4]
# x = a+b
# print(len(x))
# print(x)

A, B, C = map(int, input().split(' '))


print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)