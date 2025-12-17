from collections import deque

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
	queue = deque()
	queue.append(x, y)
	
    # 큐가 빌 때까지 반복하기
	while queue:
        x, y = queue.popleft()
		# 현재 위치에서 네 가지 방향으로 위치 확인
		for i in range(4):
            nx = x + 