# finding min
a = [1,2,3,4,5]
min = 6
for i in a:
    if i < min:
        min = i
print(min)

# 정렬 - 선택정렬 O(N^2)
arr = [5,4,2,3,1]
print("정렬 전: ", arr)
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
    print(i,"번째 정렬: ", arr)
print("정렬 후: ", arr)

# 정렬 - 버블정렬 O(N^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i): 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [5,9,1,3,4,2,8,6,7]
print("정렬 전: ", arr)
bubbleSort(arr)
print("정렬 후: ", arr)

# 검색 - 순차검색 O(N)

# 검색 - 이진검색 O(logN)
# 그래프 - 너비우선탐색 O(N) BFS
# 그래프 - 높이(깊이)우선탐색 O(N) DFS
# 재귀 알고리즘 - 팩토리얼 
def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)
n = int(input('정수 입력: '))
print("fac = ",fac(5))
# 재귀 알고리즘 - 피보나치 
def fibo(n): # 재귀함수 - n을 받아서 n 번째 피보나치 수를 반환한다. 
    if n<=2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print("fibo = ", fibo(n))


