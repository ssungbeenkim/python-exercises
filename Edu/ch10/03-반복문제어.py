# 반복문의 제어 

# 해보기 5 
num = 1
while True:
    print('num;',num)
    num+=1
    if num%7==0:
        break

# 해보기 6
num = 1
dan = int(input('dan:'))
while num<=9:
    print(dan,'*',num,'=',dan*num)
    num+=1



# 해보기 7 위 코드를 2~n단까지 출력해보기 
dan = int(input('dan:'))
for i in range(2,dan+1,1):
    for j in range(1,10,1):
        print(i,'*',j,'=',i*j)
    print('******************')

# range 안에 두개의 수만 주면 a 부터 b-1까지이다. 
for k in range(1,10): # 1~9 . (1,10,1) 과 동일하다. 
    print(k)


# 해보기 8 n1 단 제외하고 출력하기 

n = int(input('dan:'))
n1 = int(input('제외 :'))
for i in range(2,n+1,1):
    for j in range(1,10,1):
        if i == n1:
            continue
        else :
            print(i,'*',j,'=',i*j)
    print('******************')

# 해보기 9 1 ~ 9 사이의 수로 제한하여 입력받고 구구단 출력하기

while True:
    print('1 ~ 9 number : ')
    dan = int(input())
    if(dan<1 and dan>9):
        print('again')
    if(dan>0 and dan<10):
        break
count=1
while True:
    print(dan,'*',count,'=',dan*count)
    count += 1 
    if count > 9:
        break


