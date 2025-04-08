# # 학번:              이름:

# # for i in range(3,8,4):
# #     print(i)

# # cnt=0

# # for i in range(100,10,-2):
# #     print(i)
# #     print(cnt)
# #     cnt +=1


# # for i in range(1,11,1):
# #     print(i,end='')

# ### 예시1 ###
# ### coding here ###

# # for i in range(5):
# #     print('*'*10)


# ### 예시2 ###
# # for i in range(6) :
# #     print('*'*(i+1))


# # for i in range(10):
# #     if i % 2 == 0:
# #         print(i)


# ### 예시3 ###

# # for i in range(6) :
# #     print( '*'*(5-i))

# ### 예시4 ###
# # for i in range(1,31) :
# #     if i % 3 == 0 :
# #         print(i)

# # res = 0
# # for i in range(1,11):
# #     res += i

# # print(res)

# # res = 1
# # for i in range(1,11):
# #     res = res*i

# # print(res)   

# ### 예시5 ###
# # num = int(input('2 이상의 숫자를 입력해 주세요 : '))
# ## coding here ###

# # res = 1
# # for i in range(1,num+1):
# #     res = res*i

# # print(res)

# # res = 1
# # for i in range(num,0,-1):
# #     res = res*i

# # print(res) 

# #홀수만 더하기/짝수만 더하기

# # res = 1
# # for i in range(0,11,2):


# ### 예시6 ###

# # i = 0
# # dan = 0

# # dan = int(input('구구단 몇 단을 계산할까요? : '))

# # # for i in  range(1,10) :
# # #     dan = dan*i

# # # print( dan * i )

# # for i in range(1,10):
# #     print('%d * %d = %d' %(dan,i,dan*i))

# # for i in range(5):
# #     for j in range(3):
# #         print(i,j)


# # res = 0
# # i = 0

# # while i < 11:
# #     res += 1
# #     i += 1

# # print(res)

# ### 예시7 ###

# # for i in range(2,10):
# #     for j in range(1,10):
# #         print('%d * %d = %d' %(i,j,i*j))

# #예시 7번 2*1 3*2 이렇게 지속되는 거랑 위에랑 뭐가 어케 다른 겨?


# # i=0
# # while i<5:
# #     print(i)
# #     i += 1

# # password = '651'
# # answer = input('비번')

# # if answer == password:
# #     print('정답')


# # while answer != password:
# #     answer = input('비번:')

# # print('정답')

# ### 예시8 ###
# ### coding here ###

# i = 0

# while i < 6:
#     print('*'*10)
#     i += i+1

# print(i)

i = 0
while i < 10:
    print(i)
    i += i+1
    break


for i in range(1,31):
    if i % 3 != 0:
        continue
    print(i)

i += 1
i += i+1


# ### 예시9 ###
# ### coding here ###

res = 0
for i in range(1,101):
    res += i
    print(res)

res = 0
i = 1

while i < 101:
    res =+ i
    i =+ 1
print(res)



# ### 예시10 ###
# ### coding here ###


a = 30
b = 75

for i in range(1,31):
    a % i == 0 and b % i == 0
    




res = 1
i = 1
for i in range(1,31):
    if 30%i ==0 and 75%i==0:
        res = i
    i += 1
print(res)

