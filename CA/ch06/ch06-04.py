st1 = 'kim'
st2 = 'lee'
st3 = 'park'
st4 = 'choi'
print(st1 + st2 + st3 + st4) # kimleeparkchoi

st1_score = 100
st2_score = 99
st3_score = 80
print(st1_score, st2_score, st3_score) # 100 99 80
sum = st1_score + st2_score + st3_score
print(sum) # 279
print(sum/2) # 139.5
print(sum//2) # 139 # 정수값만 나온다. 

st5_score = int(input("학생5의 성적을 입력하세요: "))
print(st5_score) # 100


print('세 과목의 성적을 입력하세요');
sub1 = float(input('sub1: '))
sub2 = float(input('sub2: '))
sub3 = float(input('sub3: '))

print(sub1, sub2, sub3)
print(type(sub1), type(sub2), type(sub3))
sum = sub1 + sub2 + sub3
avg = (sum) / 3
print(avg)
print('sub1:',sub1,'sub2:',sub2,'sub3:',sub3,'sum:',sum,'avg:',avg)
#23.0 45.0 67.0 실수형인 것을 볼 수 있다. 
#<class 'float'> <class 'float'> <class 'float'> 

# 사각형 그리기
import turtle as t
t.shape('turtle')
t.color('green','skyblue')

t.forward(100)
t.right(360/4)
t.forward(100)
t.right(360/4)
t.forward(100)
t.right(360/4)
t.forward(100)
t.right(360/4)
