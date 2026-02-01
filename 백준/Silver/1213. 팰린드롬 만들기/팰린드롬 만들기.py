from collections import Counter
name = input()
cnt = Counter(name)
odd_char = []

for char, num in cnt.items():
    if num % 2 == 1:
        odd_char.append(char)

# 홀수개인 문자가 두 개 이상이면 팰린드롬 안 됨
if len(odd_char) > 1: 
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 만들기
    front = []
    middle = ''
    
    for char in sorted(cnt.keys()):
        # front에 절반씩 추가 
        front.append(char * (cnt[char] // 2))
        if cnt[char] % 2 == 1:
            middle = char
    
    # 결과: front + middle + front 역순으로 출력
    result = ''.join(front) + middle + ''.join(front)[::-1]
    print(result)
