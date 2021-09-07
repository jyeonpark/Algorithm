# 이중 for문으로 만들기
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()

# count = 0
# for i in range(n) :
#     for j in range(i+1, n) :
#         if data[i] != data[j] :
#             count += 1

# print(count)



# 방법 2
# n, m = map(int, input().split())
# weight = list(map(int, input().split()))
# weight.sort()

# count = 0 # 볼링공 조합 개수
# sequential = 1 # 같은 숫자 개수

# for i in range(n-1) :
# 	# 같은 수 중 마지막 숫자
# 	if weight[i] != weight[i+1] :
# 		# 뒤에 있는 숫자 개수 * 자신의 같은 숫자 개수
# 		count += (n-1-i) * sequential
# 		sequential = 1
# 	else :
# 		sequential += 1

# print(count)



# 단일 for문 2개로 만들기

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무개를 담을 수 있는 리스트
array = [0] * 11

for x in data :
    # 각 무게애 해당하는 볼링공의 개수 세기
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1) :
    # 누적 볼링 개수(n) 에서 무게가 i인 볼링공 제외하기
    n -= array[i]
    
    # A가 i를 선택할 때,
    # B는 선택할 수 있는 개수는 n 
    result += array[i] * n

print(result)

'''
이중 for문으로 짰더니 너무 간단해서 시간복잡도를 줄일 수 있을 거란 예상이 들었다.
역시나 간단하게 for 문 한 개로 축약할 수 있는 문제이다.
일단, 1<=M<=10 임을 고려하여 1~10 을 저장할 수 있는 array 를 만든다.
그런 다음, 입력한 볼링공의 무게별로 array 의 인덱스에 개수를 센다.

그리고 1부터 M까지의 무게 별로 for문에서 처리를 할 수 있다.
즉, 먼저 i 무게의 볼링공을 선택하였을 때를 가정하고, 이때의 경우의 수를 구하는 것이다.
이는 볼링공의 총 개수인 n에서 array[i] (i무게의 볼링공 개수) 를 뺀 값과 array[i] 를 곱하면 된다.
서로 다른 무게여야하므로 i무게를 제외한 볼링공 개수를 곱하면 되는 것이다.
i가 증가할 때마다 n의 값은 줄어들게 되는데, 조합의 문제이기 때문에 당연한 것이다.
예로 i가 1일 때 2,3,... 무게에 대해 경우의 수를 구했다면, i가 2,3... 일 때는 1의 무게를 
선택하는 경우를 배제해야 한다. 
'''