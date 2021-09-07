'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예) N=17, K=4 라고 가정하자.
1 (16) -> 2 (4) -> 2 (1)
즉, 1이 될 때 까지의 최소 횟수는 3.

-> 최대한 K로 많이 나누는 것이 최적의 해를 보장한다!!
'''

#예제 3-4

n,k = map(int, input().split())
count = 0

while(True):
    # N이 k로 나누어 떨어지는 수가 될 때 까지 1씩 빼기
    target = (n//k) * k
    count += (n - target) 
    n = target
    if n<k : 
        break
    count += 1
    n //= k

# 방법2
# while(n >= k):
# 	if(n % k == 0):
# 		n //= k
# 		count += 1
# 	else:
# 		count += n % k
# 		n -= n % k

# 남은 수에 대해 1씩 빼기
count += (n - 1)
print(count)
    
