# 반복문 for, while

for i in range(5):
    print(i)


print('python')
print() # 한줄 띄어준다. 

for n in range(1,6,1):
    print(n) # 1~5까지 출력된다.
# python

# 1
# 2
# 3
# 4
# 5

# 조건문과 마찬가지로 들여쓰기 중요 

print('python')
print()
n = 1
while n < 5:
    print(n)
    n += 1
# python

# 1
# 2
# 3
# 4

# 1부터 n까지 합 구하기 
n = int(input('n: '))
sum = 0
for i in range(1,n+1,1):
    sum += i
print(sum)


# 별 찍기  
for i in range(5):
    print('*'*i)


for i in range(5):
    print('*'*(5-i))


# 구구단 2단 출력하기 
for i in range(1,10,1):
    print('2 *',i,'=',2*i)


# 구구단 2단부터 9단까지 출력하기
for i in range(2,10,1):
    for j in range(1,10,1):
        print(i,'*',j,'=',i*j)
    print()
    
