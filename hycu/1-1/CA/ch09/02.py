# ramdom, time 모듈

# 윤년 구하기 
year = int(input("연도를 입력하세요: "))
if((year%4==0 and year%100!=0) or year%400==0):
    print("leap year")
else:
    print("not leap year")

#random 모듈
import random 
rannum = random.randint(1,39)
print(rannum) # 1~39 사이의 임의의 정수가 출력된다. 

a = random.randint(1,10)
b = random.randint(1,10)

if(a>b): # a가 b보다 크면 a와 b를 바꾼다.
    temp = a 
    a = b
    b = temp
val = random.randint(a,b)
print('a:',a,'b:',b,'val:',val)


#time 모듈
import time

print(time.time()) #1684577699.624249
time.sleep(5) # 5초간 스레드를 멈춤
print(time.ctime()) #Sat May 20 19:14:59 2023