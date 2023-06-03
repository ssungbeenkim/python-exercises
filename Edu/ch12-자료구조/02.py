def getVal():
    a = int(input('val: '))
    return a

def add():
    a = getVal()
    b = getVal()
    return a+b

def sub():
    a = getVal()
    b = getVal()
    return a-b

def mul():
    a = getVal()
    b = getVal()
    return a*b

def div():
    a = getVal()
    b = getVal()
    return a/b

def ment():
    print('사칙연산을 수행합니다. \n 연산번호는 1:add 2:sub 3:mul 4:div 5:end 입니다.')

while True:
    ment()
    choice = int(input('연산번호: '))
    if choice == 1:
        print(add())
    elif choice == 2:
        print(sub())
    elif choice == 3:
        print(mul())
    elif choice == 4:
        print(div())
    elif choice == 5:
        print('종료합니다.')
        break
    else:
        print('잘못된 연산번호입니다. 다시 입력해주세요.')
        continue



