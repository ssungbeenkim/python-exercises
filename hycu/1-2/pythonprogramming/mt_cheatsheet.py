# f 문자열

import random as rd
import datetime as dt
import math
user_name = 'testuser'
print(f'Hello, {user_name}!')

unit_price = 9.99
quantity = 200
# , : 1000단위 ,
# .2f : 소수점 2자리까지 표시하고 이후에서 반올림 해준다.
print(f'Subtotal: ${unit_price * quantity:,.2f}')

tax_rate = 0.065
print(f"tax rate is {tax_rate:.2%}")

# 수치 데이터 처리 함수
x = -123.1234
abs_x = abs(x)
round_x = round(x)
print(f"abs_x is {abs_x}, round_x is {round_x}")

dec = 85
bin_dec = bin(dec)  # 2진수로 변환
print(f"bin_dec is {bin_dec}")

print(hex(dec))  # 16진수로 변환해서 리턴해줌
print(int(dec))
print(type(dec))

# 수치 데이터 처리 함수 및 상수 목록 출력
mathFunctionAndConstant = dir(math)
print(mathFunctionAndConstant)
print(math.e)
print(math.pi)

# 문자열
numString = "0123456789"
alphabetString = "abcdefghijklmnopqrstuvwxyz"
print("\\")
print(numString * 3)
print(numString[0])
print(numString[0:8])  # 0 ~ 8-1
print(numString[0:8:2])  # 0 ~ 8-1까지 2칸씩 건너뛰면서
print(len(numString))
print(min(numString))
print(min(alphabetString))
print(max(numString))
print(max(alphabetString))

A = 0x41
print(A)
print(chr(A))
print(ord('A'))  # 아스키 코드값 리턴

# 대문자로 변환
s = 'aBcDeFg'
print(s.upper())  # ABCDEFG
print(s.capitalize())  # Abcdefg (첫글자만 대문자 이후는 소문자로 변경함)
print(str.capitalize(s))  # Abcdefg

# 포함된 문자열 세기
st = "ststssssstst"
print(st.count('st'))  # 4
print(str.count(st, 'st'))  # 4

# now, input, random
now = dt.datetime.now()
print(now)
print(now.hour)
# answer = input("What is your name?")
# print(answer)

print(rd.randint(1, 3))
