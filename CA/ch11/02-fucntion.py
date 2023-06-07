def greeting():
    print('hello')
    print('world')
    print('!!')

greeting()
greeting()
greeting()

def add(n):
    return n,n+100 # 두개를 리턴 

n = int(input('n:'))
result = add(n)
print(result)
