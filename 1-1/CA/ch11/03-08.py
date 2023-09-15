# 해보기 8 

def test():
    global a # 함수 내에서 전역변수 선언 
    a = 3
    b = 2
    return a+b 
print(test())
print(a)