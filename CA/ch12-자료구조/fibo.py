def fibo(n): # 재귀함수 
    if n<=2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def sum(n):
    i = 1
    sum = 0
    while i <= n:
        print('fibo(',i,')=',fibo(i))
        sum += fibo(i)
        i+=1
    return sum

n = (int(input('n: ')))
print('fibo( 1 ) ~ fibo(',n,')까지의 합 =',sum(n))
