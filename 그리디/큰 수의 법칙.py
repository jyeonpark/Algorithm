''' 
큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때
            주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
            단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 
            K번을 초과하여 더해질 수 없다.

예1) 2, 4, 5, 4, 6 으로 이루어진 배열이 있을 때 M=8, K=3 이라고 가정하자.
큰 수의 법칙에 따른 결과 : 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

예2) 3, 4, 3, 4, 3 으로 이루어진 배열이 있을 때 M=7, K=2 라고 가정하자.
이 경우 두 번째 원소의 4와 네 번째 원소 4를 번갈아 두 번씩 더할 수 있음
4 + 4 + 4 + 4 + 4 + 4 + 4 = 28
 
 '''

 # 예제 3-2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += first * count 
result += second * (m-count)

print(result)
