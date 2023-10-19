score = [1, 2, 3, 4, 5]
for n in score:
    print(n)

print(1 in score)
print(len(score))
print(max(score))
print(min(score))
print(sum(score))
score.append(6)
score.insert(0, 0)
print(score)

# list 결합

score2 = [7, 8, 9]
score1plus2 = score + score2
print(score2)
print(score1plus2)
score.extend(score2)  # score2를 score에 결합
print(score)

# list 삭제
willRemove = [1, 1, 2, 2, 3, 4, 5]
willRemove.remove(1)  # 첫번째로 나오는 값만 삭제
print(willRemove)

# list.pop(index)
poped = willRemove.pop(1)  # index 1번째 값을 뽑아 리턴
print(poped)
print(willRemove)
popedLast = willRemove.pop()  # Index를 전달하지 않으며 마지막 값을 뽑아 리턴
print(popedLast)
print(willRemove)

# del
del willRemove[0]  # index 0번째 값을 삭제. * index가 범위를 벗어나면 IndexError
print(willRemove)

# del willRemove  # 인덱스를 부여하지 않으면 변수 자체를 삭제
# print(willRemove)  # NameError: name 'willRemove' is not defined

print(len(willRemove))
print(willRemove.count(2))  # 2의 개수를 리턴
print(willRemove.index(2))  # 2의 인덱스를 리턴 * 2가 없으면 ValueError


# list.clear() ->  모든 요소를 삭제
willRemove.clear()
print(willRemove)  # [] 빈 리스트가 된다.

# sort

willSort = [1, 4, 3, 5, 2, 6, 8, 9, 0]
willSort.sort()  # 오름차순 정렬
print(willSort)

willSort.sort(reverse=True)  # 내림차순 정렬 * reverse=False가 Default
print(willSort)

# keyword argument key : 정렬을 위해 값을 전처리하는 함수를 지정
# 리스트의 각 항목에 대해 kf 함수를 호출하고 그 결과를 기준으로 정렬한다.


def kf(x):
    print('kf=', x)
    return 9 - x


willSort.sort(key=kf, reverse=False)
print(willSort)  # [9, 8, 6, 5, 4, 3, 2, 1, 0]
# 오름차순 정렬을 해주었으나 kf는 9-x를 리턴하므로 9부터 0까지 내림차순으로 정렬된다.

# 대소문자 구분없이 정렬하기
students = ['Alpha', 'bravo', 'Charlie', 'delta', 'Echo']
students.sort()
print(students)  # 대소문자를 포함하여 정렬된다.

students.sort(key=str.lower)
print(students)  # 전처리 함수를 사용하여 소문자로 변환한 것을 기준으로 정렬하여 알파벤 순으로 정렬할 수 있다.

# reverse
students.reverse()
print(students)  # 리스트를 역순으로 뒤집는다.

# copy
studentsCopy = students.copy()
print(studentsCopy)  # students의 복사본을 리턴한다.

# 리스트 비교
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [1, 2, 4, 2]
print(list1 == list2)  # True
print(list1 == list3)  # False
print(list1 <= list2)  # True
# True * list3에서 list1과 왼쪽부터 동일 위치 항목을 비교하여 하나라도 큰 값이 있으면 True
print(list1 <= list3)  # True
print(list1 < list3)  # True
# 만약 틀린것이 먼저 발견된다면 Falsef가 리턴된다.
