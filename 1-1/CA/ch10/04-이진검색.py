# 이진검색 
# 반복문의 활용 

# 해보기 1 - 1~100 수 중 2의 배수이거나 7의 배수인 경우의 합
# # while
sum = 0
i = 0
n = int(input('type number:'))
while i <= n:
    if i%2 == 0 or i%7==0:
        sum += i
    i += 1
print('sum=',sum)

print()
# # for 

sum = 0

for i in range(n+1):  #! 
    if i%2 == 0 or i%7 == 0:
        sum += i
print('sum is',sum);

# 연습문제2

while True:
    a = int(input('press numbre a:'))
    b = int(input('press numbre b:'))
    if(b<=a):
        print('b must be bigger than a')
        continue
    else:
        break
    
print('a:',a,'b:',b)
sum = 0
for i in range(a,b+1):
    if i%2 == 0 and i%3 != 0:
        sum += i
print('sum:',sum)

# 연습문제 3 - 이진 검색 
# a and b 사이 검색값을 찾는 알고리즘 

a = 1
b = 99999999
n = 0
while n>b or n<a:
    n = int(input('n:'))

print('n:',n)

i=1
while True:
    m = (a+b)//2
    print(i,'번째','m:',m)
    if m == n:
        print('성공',i,'번만에 찾았다.')
        break
    elif n > m:
        a = m
    elif m > n:
        b = m
    i += 1

# 연습문제 4

while True:
    dan = int(input('구구단을 출력. 1~9까지 숫자를 하나 입력'))
    if(dan>=1 and dan<=9):
        print('dan:',dan)
        break
    print('다시 입력하시오')
count = 1
while True:
  print(dan,'*',count,'=',dan*count)
  if count == 9 :
    break
  count += 1

# 연습문제 5

dan = int(input('몇단까지 출력할까요?'))
print('dan:',dan)

i = 1
while True:
    print('[',i,'단]')
    count = 1
    while True:
        print(i,'*',count,'=',i*count,end=' ') # !! end
        if count == 9 :
          break
        count += 1
    i+= 1
    print('')
    print('')
    print('')
    if i > dan:
        break

# 연습문제 6

sum = 0
i = 1
while i<=100:
    if(i%3==0 and i%5==0):
        print(i,end=',')
        sum += i
    i += 1
print()
print('sum:',sum)

