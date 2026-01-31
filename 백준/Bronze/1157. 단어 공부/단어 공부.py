str = input()
dic = {}

for char in str.upper():
    dic[char] = dic.get(char, 0) + 1

max_value = max(dic.values())

# 최대값이 여러 개인지 확인
if list(dic.values()).count(max_value) > 1:
    print("?")
else:
    print(max(dic, key = dic.get))