def solution(participant, completion):
    
    dict_part = {}
    
    # 1. 참가자, 참가자 수 딕셔너리에 넣기
    for name in participant:
        dict_part[name] = dict_part.get(name, 0) + 1
        
    # 2. 참가자에서 완주자 수 만큼 -1
    for name in completion:
        dict_part[name] -= 1
        
    # 3. 완주하지 못 한 참가자 찾기
    for name in dict_part:
        if dict_part[name] > 0:
            answer = name 
            break
            
    return answer