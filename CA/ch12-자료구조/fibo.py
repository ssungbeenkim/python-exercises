def fibo(n): # 재귀함수 - n을 받아서 n 번째 피보나치 수를 반환한다. 
    if n<=2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def sum(n): # n번째 피보나치 수까지의 합을 반환. 
    i = 1
    sum = 0
    while i <= n:
        print('fibo(',i,')=',fibo(i))
        sum += fibo(i)
        i+=1
    return sum

n = (int(input('n: ')))
print('fibo( 1 ) ~ fibo(',n,')까지의 합 =',sum(n))
