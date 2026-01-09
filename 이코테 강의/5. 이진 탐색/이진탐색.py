# 이진 탐색 소스코드 (재귀적)
def binary_search(array, target, start, end):
    # 시작점이 끝점보다 클 경우 엇갈린 것이기에 찾는 데이터가 없는 것임 
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점의 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end) 
    
# 이진 탐색 소스 코드 (반복문)
def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 변환
        if array[mid] == target:
            return mid
        # 중간값의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None 

# n(원소의 개수)과 target(찾고자 하는 데이터)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search_while(array, target, 0, n -1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
