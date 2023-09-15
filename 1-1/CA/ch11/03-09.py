a = 10

def test():
    global a # 전역변수로 선언하고  
    a = 1 # 1로 변경하였다. 
    b = 2
    return a+b
print(test()) # 3
print(a) # 1