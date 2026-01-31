sw_num = int(input())
switchs = [-1] + list(map(int, input().split()))

st_num = int(input())
# 스위치 바꾸는 함수
def change(index):
    if switchs[index] == 0:
        switchs[index] = 1
    else:
        switchs[index] = 0

for s in range(st_num):
    sex, num = map(int, input().split())
    
    # 남자일 때
    if sex == 1:
        for i in range(num, len(switchs)):
            if i % num == 0:
                change(i)
    # 여자일 때
    else:
        # 받은 번호 스위치 변경
        change(num)
        i = 1
        while num - i >= 1 and num + i <= sw_num:
            if switchs[num - i] == switchs[num + i]:
                change(num - i)
                change(num + i)
                i += 1
            else:
                break
                
# 출력 형식 (20개씩 끊어서)
for i in range(1, sw_num + 1):
    print(switchs[i], end=' ')
    if i % 20 == 0:
        print()