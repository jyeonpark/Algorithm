import heapq

def solution(food_times, k):
    answer = 0

    # 음식 시간의 총 합이 k와 같거나 작으면 
    # 다음으로 먹을 음식이 없는 것이므로 -1 리턴
    if (sum(food_times) <= k) :
        return -1

    # 우선순위 큐
    q = []
    for i in range(len(food_times)) :
        # (음식 시간, 음식 번호) 형태로 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    length = len(food_times) # 남은 음식 개수
    sum_value = 0 # 한 음식을 다 먹기 위해 걸린 시간
    prev = 0 # 이전에 음식을 먹는데 걸린 시간

    # 남은 음식 개수 * (제일 작게 걸리는 음식 시간 - 이전에 먹은 시간) 이 
    # k - (지금까지 먹은 시간) 보다 작거나 같을 때 반복하기
    # -> 한 음식을 다 먹을 수 있으면 반복문 실행
    while (length * (q[0][0] - prev) <= (k - sum_value)):
        # 시간이 가장 작게 걸리는 음식을 pop 하고, now에 저장
        now = heapq.heappop(q)[0]
         # [(한 음식을 먹는데 걸리는 총 시간) - (이전까지 먹은 시간)] * 음식 개수
        sum_value += (now - prev) * length
        length -= 1 # 음식 개수 하나 빼기
        prev = now

    # 남은 음식 중에서 몇 번째 음식인지 확인
    result = sorted(q, key=lambda x: x[1]) # 번호 순대로 오름차순 정렬
    return result[(k - sum_value) % length][1]

print(solution([8,6,4],15))