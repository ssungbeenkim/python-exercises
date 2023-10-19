# 특징
# 파이썬의 가장 단순한 복합 데이터 유형임
# 원소를 항목(item)이라 함
# 파이썬의 튜플 데이터 유형 이름은 "tuple"임
# 각 항목(item)의 유형을 임의로 정할 수 있음
# 각 항목을 인덱스 연산자를 통해 임의로 또는 랜덤하게
# 액세스할 수 있음
# 각 항목을 in 연산자를 통해 순차적으로 읽어내어 객체 참조에
# 배정할 수 있음
# 튜플은 값을 변경할 수 없는(immutable) 데이터 유형임
# 즉, 튜플 항목을 추가, 삭제, 값의 변경을 할 수 없고 항목의
# 배열 순서도 바꿀 수 없음

tuple1 = (1, 'two', 3.0, 'four')
print(tuple1)
print(tuple1[1])
print('two' in tuple1)
print(len(tuple1))

print("start print")
for e in tuple1:
    print(e)
print("all printed")

# 횟수 계산하기
tuple2 = (1, 2, 3, 2, 4, 2)
print(tuple2.count(2))
print(tuple2.index(2))  # 첫번째 2의 인덱스를 리턴 * 2가 없으면 ValueError

if (100 in tuple2):  # 튜플에 있는지 확인해서 적절히 출력
    print("100 is in tuple2")
else:
    print("100 is not in tuple2")

# concat
concatedTuple = tuple1 + tuple2
print(concatedTuple)  # 순서를 유지하면서 새로운 튜플 생성됨.

# comparison

tuple3 = (1, 2, 3, 4)
tuple4 = (1, 2, 3, 5)

print(tuple3 == tuple4)  # False
print(tuple3 < tuple4)  # True
