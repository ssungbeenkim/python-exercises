# 이진검색 
# 반복문의 활용 

# 해보기 1 - 1~100 수 중 2의 배수이거나 7의 배수인 경우의 합

# # while

# sum = 0
# i = 0
# n = int(input('type number:'))
# while i <= n:
#     if i%2 == 0 or i%7==0:
#         sum += i
#     i += 1
# print('sum=',sum)

# print()
# # for 

# sum = 0

# for i in range(n+1):  #! 
#     if i%2 == 0 or i%7 == 0:
#         sum += i
# print('sum is',sum);

# 연습문제2

while True:
    a = int(input('press numbre a:'))
    b = int(input('press numbre b:'))
    if(b<=a):
        print('b must be bigger than a')
        continue
    else:
        break
for i in range(a,b+1):
    if i%2 == 0 and i%3 != 0:
        print(i)
