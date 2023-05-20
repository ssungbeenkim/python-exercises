
# 5명의 학생들의 성적을 랜덤으로 출력하기 
import random as rd
for i in range(5):
    print('score of student',i+1,':',rd.randint(0,100))


# 해보기 10 

sum = 0
for i in range(5):
    score = rd.randint(0,100)
    print('score',score)
    sum += score 

avg = sum/5
print('avg:',avg)

# 해보기 11 

sum = 0
min = 999
max = -1
for i in range(5):
    score = rd.randint(0,100)
    print('score',score)
    if score < min:
        min = score
    if score > max:
        max = score
    sum += score 

avg = sum/5
print('avg:',avg)
print('min:',min,'max:',max)


# 해보기 12 
count = 0
sum = 0
for i in range(5):
    score = rd.randint(0,100)
    print('score',score)
    if score >= 90:
        count += 1
    sum += score 

avg = sum/5
print('avg:',avg)
print('90점 이상:',count,'명')








