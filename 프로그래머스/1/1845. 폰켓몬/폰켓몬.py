def solution(nums):
    answer = 0
    
    # 가져갈 수 있는 수 
    num = len(nums) // 2
    
    # 폰켓몬 종류의 수
    types = len(set(nums))
    
    # 가져갈 수 있는 수는 정해져 있기에 둘 중 더 작은값 선택
    answer = min(num, types)
    
    return answer