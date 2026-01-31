n = int(input())
people = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    people.append((age, name))
    
sorted_people = sorted(people, key = lambda x : x[0]) 
# 튜플에서는 명시적으로 첫 번째 값으로 정렬 sorted(members)

for age, name in sorted_people:
    print(age, name)