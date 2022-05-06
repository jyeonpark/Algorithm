def solution(participant, completion):
    hash = {} # key: 참가자 이름, value: 완주자 숫자를 담은 해시 딕셔너리
    
    for i in participant :
        if i in hash : # 해시테이블에 존재하는 이름이라면
            hash[i] += 1
        else :
            hash[i] = 1
    
    for i in completion :
        if hash[i] == 1 :
            del hash[i]
        else :
            hash[i] -= 1
            
    return list(hash.keys())[0]
