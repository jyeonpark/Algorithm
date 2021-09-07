# 비효율적인 코드
# n, m, k = map(int, input().split())

# team = 0
# # m의 수에 맞춰 팀 개설 가능
# if (n >= 2 * m) :
#     team = m
#     n -= m * 2
#     m = 0 

# # n의 수에 맞춰 팀 개설 가능
# else :
#     team = n // 2
#     m -= n // 2
#     n -= (n // 2) * 2

# while (m > 0 and k > 0) :
#     m -= 1
#     k -= 1
# while (n > 0 and k > 0) :
#     n -= 1
#     k -= 1
# while(k > 0):
#     if (k >= 3) :
#         n -= 2
#         m -= 1
#         team -= 1
#         k -= 3
#     else :
#         n -= k
#         team -= 1
#         k = 0

# print(team)

n, m, k = map(int, input().split())
team = 0
while(n >= 2 and m >= 1 and n+m-3 >= k) :
    n -= 2
    m -= 1
    team += 1
print(team)

