n = int(input())
data = list(input().split())
# L: 왼쪽으로 한 칸 이동(서) R: 오른쪽으로 한 칸 이동(동) U: 위로 한 칸 이동(북) D: 아래쪽으로 한 칸 이동(남)

x, y = 1, 1 # 현재 위치 행과 열  

for i in range(len(data)): 

    if data[i] == 'L':
        # L로 이동했을 때 범위를 벗어나는 경우는, 맨 왼쪽에 있을 때 -> 열이 1일 때 
        if y != 1:
            y -= 1
    elif data[i] == 'R':
        # R로 이동했을 때 범위를 벗어나는 경우는, 맨 오른쪽에 있을 때 -> 열이 N일 때 
        if y != n:
            y += 1
    elif data[i] == 'U':
        # U로 이동했을 때 범위를 벗어나는 경우는, 맨 위에 있을 때 -> 행이 1일 때 
        if x != 1:
            x -= 1
    elif data[i] == 'D':
        # D로 이동했을 때 범위를 벗어나는 경우는, 맨 아래에 있을 때 -> 행이 N일 때 
        if x != n:
            x += 1

print(x, y)