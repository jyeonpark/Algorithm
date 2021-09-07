n, k = map(int, input().split())
coin = []
for i in range(n) :
    coin.append(int(input()))

coin.sort(reverse = True)
count = 0

for i in coin :
    if (k == 0):
        break
    else :
        count += k // i
        k -= i * (k//i)

print(count)