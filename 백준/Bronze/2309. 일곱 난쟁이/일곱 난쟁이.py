short = list()
for i in range(9):
    short.append(int(input()))
short_sum = sum(short)

flag = False
for i in range(9):
    if flag:
        break
    for j in range(i + 1, 9):
        real_short = short_sum - (short[i] + short[j])
        if real_short == 100:
            del short[j]
            del short[i]
            flag = True
            break

short.sort()
for height in short:
    print(height)