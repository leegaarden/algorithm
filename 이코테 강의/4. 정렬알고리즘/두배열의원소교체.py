N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))\

a.sort() # a는 오름차순으로 정렬
b.sort(reverse=True) # b는 내림차순으로 정렬

for i in range(K):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때, 반복문 탈출 -> 꼭 k번 바꿔치기 해야 하는 것 아님 
        break

print(sum(a)) # 배열 a의 모든 원소 합을 출력 