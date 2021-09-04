
data = list(map(int,input()))

result = 0

for i in data :
    if i <=1 or result <=1 :
        # 0또는 1이면 더하기
        result += i
    else:
        # 나머지는 곱하기
        result *= i
print(result)


'''
두 수에 대해서 연산을 수행할 때, 두 수 중 하나라도 0또는 1이면 더하는 것이 효율적이다.
0을 곱하면 0 이고, 1을 곱하면 자기 자신 그대로 이기 때문이다.
이러한 원리로, result(지금까지 총 계산한 것) 또는 현재 연산할 수(i)가 1 이하라면
더하기, 나머지 경우에는 곱하기 연산을 해 주면 된다.

'''