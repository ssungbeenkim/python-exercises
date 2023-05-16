a = int(input("숫자를 입력하세요: "))
b = int(input("숫자를 입력하세요: "))
result = a + b;
print(a, "+", b, "=", result)
result = a - b;
print(a, "-", b, "=", result)
result = a * b;
print(a, "*", b, "=", result)
result = a / b;
print(a, "/", b, "=", result)

# 숫자를 입력하세요: 70
# 숫자를 입력하세요: 100
# 70 + 100 = 170
# 70 - 100 = -30
# 70 * 100 = 7000
# 70 / 100 = 0.7

import turtle

turtle.shape("turtle")

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)

turtle.done()