n = int(input())
pillars = []
for i in range(n):
    l, h = map(int, input().split())
    pillars.append((l, h))

# 왼쪽 위치 기준으로 정렬
pillars.sort()

# 왼쪽 끝과 오른쪽 끝 위치
left = pillars[0][0]
right = pillars[-1][0] + 1  # 폭이 1이므로 +1

# 왼쪽에서 오른쪽으로: 각 위치의 지붕 높이 저장
roof = [0] * (right - left + 1)

# 왼쪽에서 오른쪽으로 스위프
max_height = 0
pillar_idx = 0
for x in range(left, right + 1):
    # 현재 위치에 기둥이 있으면 높이 갱신
    if pillar_idx < n and pillars[pillar_idx][0] == x:
        if pillars[pillar_idx][1] > max_height:
            max_height = pillars[pillar_idx][1]
        pillar_idx += 1
    roof[x - left] = max_height

# 오른쪽에서 왼쪽으로 스위프
max_height = 0
pillar_idx = n - 1
for x in range(right, left - 1, -1):
    # 현재 위치에 기둥이 있으면 높이 갱신
    if pillar_idx >= 0 and pillars[pillar_idx][0] == x:
        if pillars[pillar_idx][1] > max_height:
            max_height = pillars[pillar_idx][1]
        pillar_idx -= 1
    # 왼쪽에서 구한 값과 오른쪽에서 구한 값 중 작은 값이 실제 지붕
    roof[x - left] = min(roof[x - left], max_height)

# 넓이 계산 (왼쪽 끝~오른쪽 끝까지)
area = 0
for i in range(right - left):
    area += roof[i]

print(area)