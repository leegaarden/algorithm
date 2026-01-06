# str = input()

# c = str[0] # 열
# r = str[1] # 행

# # 나이트가 갈 수 있는 경우의 수는 최대 8가지 
# # 이 8가지 중에서 안 되는 걸 -1 하는 식으로 구현

# count = 8

# # 1. 왼 왼 위 -> 열이 a or b or 행이 1
# if c <= 'b' or r == '1':
#     count -= 1
# # 2. 왼 왼 아래 -> 열이 a or b or 행이 8
# if c <= 'b' or r == '8':
#     count -= 1
# # 3. 오 오 위 -> 열이 g or h or 행이 1
# if c >= 'g' or r == '1':
#     count -= 1
# # 4. 오 오 아래 -> 열이 g or h or 행이 8
# if c <= 'g' or r == '8':
#     count -= 1
# # 5. 위 위 왼 -> 행이 1 or 2 or 열이 a
# if r >= '1' or c == 'a':
#     count -= 1
# # 6. 위 위 오 -> 행이 1 or 2 or 열이 h
# if r >= '1' or c == 'h':
#     count -= 1
# # 7. 아래 아래 왼 -> 행이 7 or 8 or 열이 a
# if r >= '7' or c == 'a':
#     count -= 1
# # 8. 아래 아래 오 -> 행이 7 or 8 or 열이 h
# if r >= '7' or c == 'h':
#     count -= 1

# print(count)


# 내 코드의 문제점: 중복 발생
# 내 코드와 다른점: steps를 정의하여 행과 열의 수를 비교함 
# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
(2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
	# 이동하고자 하는 위치 확인
	next_row = row + step[0]
	next_column = column + step[1]
	# 해당 위치로 이동이 가능하다면 카운트 증가
	if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
		result += 1
print(result)