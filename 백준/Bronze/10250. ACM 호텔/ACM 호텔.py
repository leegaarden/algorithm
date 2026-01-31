test_case = int(input())

for i in range(test_case):
    H, W, N = map(int, input().split())
    if N % H != 0:
        y = N % H
        x = N // H + 1
    else:
        y = H
        x = N // H
   
    print(y * 100 + x)