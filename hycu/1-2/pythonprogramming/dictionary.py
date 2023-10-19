# <key>는 불가변성(immutable) 유형의 객체이어야 함(모든
# 원시 데이터 유형, str, tuple)
# <value>는 임의 유형의 문자적 값 또는 참조임
# <key>는 한 dictionary 객체 안에서 유일무이(唯一無二,
# unique)해야 함(이 점은 동음이의어가 허용되는 실제의
# 사전과 다른 점임)

dic1 = {1: 'one', 2: 'two', (3, 4): 'three'}
print(dic1)
print(dic1[2])  # index가 아니라 key로 접근
print(dic1[(3, 4)])


# dic2 = {1: 'one', 2: 'two', [3, 4]: 'three'}
# print(dic2)  # TypeError: unhashable type: 'list'
# key는 불변성을 가져야 하므로 list는 사용할 수 없다.

dic3 = {1: 'one', 2: 'two', 'three': [3, 4]}
print(dic3)
print(dic3['three'])

# dict() 함수를 사용하여 dictionary 객체 생성

# mapping dictionary를 인수로 전달하여 dictionary 객체 생성
dic4 = dict({1: 'one', 2: 'two', 3: 'three'})
print(dic4)

# iterable of iterable-of-key-value-pairs를 인수로 전달하여 dictionary 객체 생성
# dic5 = dict([[1, 'one'], (2, 'two'), {3, 'three'}]) # list로 묶어서
dic5 = dict(([1, 'one'], (2, 'two'), {3, 'three'}))  # tuple로 묶어서
print(dic5)

# keyword argument를 사용하여 dictionary 객체 생성
# dic6 = dict(1='one', 2='two', 3='three') # SyntaxError: keyword can't be an expression
dic6 = dict(one=1, two=2, three=3)
# 1,2,3 등의 값은 LHS identifier가 될 수 없으므로 문법 오류가 발생
print(dic6)

# 항목 삭제하기
delobj = {1: 'one', 2: 'two', 3: 'three'}
del delobj[2]
print(delobj)

# dic 객체 참조 삭제
dic_obj = {1: 'one', 2: 'two', 3: 'three'}
print(dir())
del dic_obj
print(dir())
# print(dic_obj)  # NameError: name 'dic_obj' is not defined

# 반복문
iterDic = {1: 'one', 2: 'two', 3: 'three'}
for key in iterDic:
    print(key, iterDic[key])
print("all printed")
print('for loop done')

# .fromkeys()

fromkeysDic = dict.fromkeys([1, 2, 3], 'number')
print(fromkeysDic)  # {1: 'number', 2: 'number', 3: 'number'}

# .get()

getDic = {1: 'one', 2: 'two', 3: 'three'}
print(getDic.get(1))  # one

# .items()

itemsDic = {1: 'one', 2: 'two', 3: 'three'}
print(itemsDic.items())  # dict_items([(1, 'one'), (2, 'two'), (3, 'three')])

# .keys()

keysDic = {1: 'one', 2: 'two', 3: 'three'}
print(keysDic.keys())
# dict_keys([1, 2, 3]) => iterable in 가능하지만 index로 접근은 불가능하다.

# .pop()

popDic = {1: 'one', 2: 'two', 3: 'three'}
print(popDic.pop(1))  # one => key 1의 value를 리턴하고 원본에서 삭제
print(popDic)  # {2: 'two', 3: 'three'}


# .popitem()

popitemDic = {1: 'one', 2: 'two', 3: 'three'}
print(popitemDic.popitem())  # (3, 'three') => 임의의 항목을 튜플로 리턴하고 원본에서 삭제
print(popitemDic)  # {1: 'one', 2: 'two'}

# .setdefault()

setdefaultDic = {1: 'one', 2: 'two', 3: 'three'}
print(setdefaultDic.setdefault(1))
# one => key 1의 value를 리턴
print(setdefaultDic.setdefault(4, 'four'))
# four => key 4가 없으므로 key 4를 생성하고 value를 리턴
print(setdefaultDic)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# .update()

updateDic = {1: 'one', 2: 'two', 3: 'three'}
updateDic.update({4: 'four'})
print(updateDic)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
updateDic.update({1: 'first'})
print(updateDic)  # {1: 'first', 2: 'two', 3: 'three', 4: 'four'}

# .values()

valuesDic = {1: 'one', 2: 'two', 3: 'three'}
print(valuesDic.values())  # dict_values(['one', 'two', 'three'])
