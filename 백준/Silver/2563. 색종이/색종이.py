p = int(input())
# 100, 100 도화지 
paper = [[0] * 100 for _ in range(100)]

for i in range(p):
    start, end = map(int, input().split())
    for s in range(start, start + 10):
        for e in range(end, end + 10):
            paper[s][e] = 1
            
aera = sum(sum(row) for row in paper)
print(aera)