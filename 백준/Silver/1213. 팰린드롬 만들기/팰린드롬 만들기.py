from collections import Counter

name = input()
count = Counter(name)

# 홀수 개인 문자 찾기
odd_chars = []
for char, cnt in count.items():
    if cnt % 2 == 1:
        odd_chars.append(char)

# 홀수 개가 2개 이상이면 불가능
if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 만들기
    front = []
    middle = ''
    
    # 알파벳 순으로 정렬
    for char in sorted(count.keys()):
        # 앞부분에 절반씩 추가
        front.append(char * (count[char] // 2))
        # 홀수 개면 가운데 문자로
        if count[char] % 2 == 1:
            middle = char
    
    # 결과: 앞 + 가운데 + 앞의 역순
    result = ''.join(front) + middle + ''.join(front)[::-1]
    print(result)