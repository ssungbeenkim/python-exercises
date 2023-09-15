# 연습문제 8 팩토리얼 구하기 

def getVal():
    n = int(input('press Number:'))
    return n 

def fac(n):
    
    fac = 1;
    for i in range(1,n+1):
        fac *=i
    return fac

val = getVal()
factor = fac(val)

# print(val,'의 펙토리얼:',factor)

