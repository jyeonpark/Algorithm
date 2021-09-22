n = list(input())

# 30의 배수란
# 1) 끝자리가 0이다.
# 2) 모든 자리수의 합이 3의 배수이다.

# 내림차순
n.sort(reverse=True)
sum = 0

if n[-1] != "0" :
    print(-1)
else :
    for i in n :
        sum += int(i)
    if sum % 3 != 0 :
        print(-1)
    else :
        print(''.join(n))
