# 자료구조는 데이터의 형식 

# 파이썬의 자료구조 

# 1. List 

a = [1,2,3,4,5]
print(type(a)) # <class 'list'>

# index 를 통하여 검색, 변경이 가능하다. 
a[0] = 99
print(a[0]) # 99

# 다양한 자료형을 item으로 가질 수 있다. 
#a = [1,'hi,3]
#a = [1,2,[1,2,3,4]]

# 사용 함수 
a.append(6)
print(a) # [1, 2, 3, 4, 5, 6]
del a[0]
print(a) # [2,3,4,5,6]

# 반복문 
for i in a:
    print(i*2) 

# 2. tuple 
# 리스트와 유사하지만 값의 변경, 삭제가 불가. 순서가 정해져 있는 객체들의 집합. 

a = (5,4,3,2,1)
print(type(a)) # <class 'tuple'>
print(a[0]) # 5 

# 값의 추가는 안되고, 튜플끼리 더해서 추가가 가능하다. 
a = a + (2,3)
print(a) # (5, 4, 3, 2, 1, 2, 3)

a = a + (4,) # ! , 를 안쓰면 에러. 
print(a) #(5, 4, 3, 2, 1, 2, 3, 4)

# 3. Dcitionary 
# 키와 값을 가지고 키를 통해 값에 접근 가능하며 값을 통한 접근 불가. javacript의 object 
a = {'a':'dkfj',1:'aslkdfj'}
print(type(a)) # <class 'dict'>
print(a['a']) # 딕셔너리의 키는 변수 또는 상수 값이어야 한다. 
print(a[1])

print(a.keys()) # dict_keys(['a', 1])
print(a.values()) #dict_values(['dkfj', 'aslkdfj']) 

del a['a'] # 키를 통한 삭제
print(a)

b = {'c':'blah',2:'sldkjf'}
a.update(b) # a에 b를 추가
print(a)

# 4. set
# 데이터를 중복없이 관리. 집합연산(&,|,-,^) 가능
a = {1,2,3,4}
print(type(a)) # <class 'set'>
b = {2,3,4,5}

print(a&b) # {2, 3, 4} 교집합
print(a|b) # {1, 2, 3, 4, 5} 합집합
print(a-b) # {1} 차집합
print(a^b) # {1, 5} exclusive 배타

