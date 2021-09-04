
s = list(map(int,input()))
count0 = s.count(0)
count1 = s.count(1)

# 한 번에 뒤집을 개수
count = 0
total = 0

if count0 > count1 :
    num = 0
else:
    num = 1

for i in s :
    if i == num :
        if count>0 :
            total += 1
        count = 0

    else :
        count += 1

if count >0 :
    total +=1

print(total)