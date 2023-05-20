# 조건문과 반복문 예제 실습 

# 해보기 1 

print('what a wonderful world!')
number = 1
while number <= 5:
    print('python good!')
    number = number + 1

print()
# for문으로 변환하기 

for i in range(5):
    print('python good!')

# 단을 입력받아 구구단 출력하기 
""" dan = int(input())
print('***************')
for i in range(9):
    print(dan,'*',i+1,'=',dan*(i+1))
print('***************') """

# 해보기 3 - 1~10 사이의 임의의 수 맞추기 
""" import random as rd
val = rd.randint(1,10)
guess = int(input('guess number: '))
if guess == val:
    print('congratulations ','val:',val)
elif guess > val :
    print('down')
elif guess < val :
    print('up')
print('val is ',val) """

# 해보기 4 - 이전 문제 맞출 때까지 무한 반복하도록 하기 
""" 
import random as rd
val = rd.randint(1,10)
guess = 0
while guess != val:
    guess = int(input('guess number: '))
    if guess == val :
        print('congratulations ','val:',val)
    elif guess > val :
        print('down')
    elif guess < val :
        print('up')


print('val is ',val)
 """
# 이렇게 하면 더 깔끔하게도 가능하다. 
import random as rd
val = rd.randint(1,10)
guess = 0
while True:
    guess = int(input('guess number: '))
    if guess == val :
        print('congratulations ','val:',val)
        break
    elif guess > val :
        print('down')
    elif guess < val :
        print('up')

