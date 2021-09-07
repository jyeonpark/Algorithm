import heapq

def solution(food_times, k):

    if (sum(food_times) <= k) :
        return -1

    heap = []
    for i in range(len(food_times)):
    	heapq.heappush(heap, (food_times[i], i+1))
    	
    time = 0 # 이전 음식을 다 먹기 위해 걸린 시간
    total_time = 0
    food_count = len(food_times) # 남아있는 음식 개수
    
    # heap[0][0] - time -> 현재 음식을 다 먹는데 걸리는 시간 - 이전에 먹은 시간
    while((heap[0][0] - time) * food_count <= k - total_time):
        total_time += ( heap[0][0] - time ) * food_count # (음식 시간 - 이전에 먹었던 음식 시간) * 음식 개수 
        time = heap[0][0] # 한 음식을 다 먹는데 걸리는 시간
        heapq.heappop(heap)
        food_count -= 1
    	
    result = sorted(heap, key = lambda x : x[1])
    return(result[(k-total_time) % food_count][1])
    
print(solution([3,1,2],5))