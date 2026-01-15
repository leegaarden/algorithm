n = int(input())
k = list(map(int, input().split()))
result = list()

for i in range(len(k)):
    for j in range(len(k)):
        if j == i or j == (i + 1) or j == (i - 1):
            continue
        result.append(k[i] + k[j])

print(result)
print(max(result)) 