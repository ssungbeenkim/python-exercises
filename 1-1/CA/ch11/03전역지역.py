def test():
    a=3
    b=2
    return a+b
print(test()) # 함수 실행이 종료되며 지역변수는 사라진다. 
print(a) # NameError: name 'a' is not defined


