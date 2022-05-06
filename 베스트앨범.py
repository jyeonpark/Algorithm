def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}
    # dic 에 key : 장르, 
    # value : 장르 총 재생횟수 를 저장한다.
    
    # dic2 에 key : 장르,
    # value : (수록곡 재생횟수, 고유번호) 을 저장한다.
    for i, (j,k) in enumerate(zip(genres, plays)):
        if j not in dic :
            dic[j] = plays[i]
        else :
            dic[j] += plays[i]
        if j not in dic2 :
            dic2[j] = [(plays[i], i)]
        else :
            dic2[j].append((plays[i],i))
    
    # dic 의 (key, value) 에 대해 value 값으로 내림차순 정렬한다.
    for i, _ in sorted(dic.items(), key=lambda x:x[1], reverse=True) :
        # dic2 의 key 값이 i인 values 에 대해서, (수록족 재생횟수의 내림차순, 고유번호의 오름차순) 순서대로 정렬한다. 이때 values list 중 0,1번째 인덱스에 대해서만 다룬다.
        for j, k in sorted(dic2[i], key=lambda x: (-x[0], x[1]))[:2] :
            answer.append(k)
    return answer
