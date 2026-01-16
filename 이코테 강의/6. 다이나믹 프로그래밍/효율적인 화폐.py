# 화폐 가치의 개수 n, 만들어야 하는 돈 m
n, m = map(int, input().split())
# 화폐 가치 종류
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * 101

for i in array:
    if m % i == 0:
        d[i] = m / i

result = 0
if min(d) == 0:
    result = -1
else:
    result = int(min(d))

print(result)

# 강의 코드 (위 코드는 틀렸음)
# 화폐 가치의 개수 n, 만들어야 하는 돈 m
n, m = map(int, input().split())
# 화폐 가치 종류
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0

for i in range(n): # i는 각각의 화폐 단위를 의미
    for j in range(array[i], m + 1): # j는 각각의 금액을 의미
        if d[j - array[i]] != 10001: # (i-K)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1) 

# 계산된 결과 출력
if d[m] == 10001: #최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
