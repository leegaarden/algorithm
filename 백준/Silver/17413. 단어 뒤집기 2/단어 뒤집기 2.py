word = input()
result = ''
temp = ''
in_tag = False

for char in word:
    if char == '<':
        # 태그 시작 전에 모인 단어들 처리
        result += temp[::-1]
        temp = ''
        in_tag = True
        result += char
    elif char == '>':
        in_tag = False
        result += char
    elif in_tag:
        # 태그 안에서는 그대로
        result += char
    elif char == ' ':
        # 공백 만나면 temp 뒤집어서 추가
        result += temp[::-1] + ' '
        temp = ''
    else:
        # 일반 문자는 temp에 모으기
        temp += char

# 마지막 남은 temp 처리
result += temp[::-1]
print(result)