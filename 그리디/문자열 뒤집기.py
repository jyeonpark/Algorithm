str = list(map(int,input()))

one = 0 # 0을 뒤집는 횟수
zero = 0 # 1을 뒤집는 횟수
last = -1 # 이전 숫자

for i in str :
    # i가 1이고, 연속된 1이 아닐 때
	if (i == 0 and last != 0):
		zero += 1
    # i가 0이고, 연속된 0이 아닐 때
	elif (i == 1 and last != 1):
		one += 1
	last = i
print(min(zero, one))