'''
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다.
2. 뽑고자 하는 카드가 포함된 행을 선택한다.
3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
-> 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것!!!
'''

# 예제 3-3
n, m = map(int, input().split())
result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    # 각 행에서 가장 작은 값
    min_value = min(data)

    # 행에서 가장 작은 값들 중 가장 큰 값
    result = max(result, min_value)

print(result)