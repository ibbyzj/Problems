#Python program to run the Flower problem - store users in a heap incase number of users is less than the number of flowers
import sys
import heapq

userHeap = []
number_Flowers, number_People = raw_input().split()
number_People= int(number_People)
number_Flowers = int(number_Flowers)

C = map(int,raw_input().split(' '))
C.sort(reverse=True)
cost = 0
index = 1

if(number_People >= number_Flowers):
	while(index <= len(C)):
		cost = cost + C[index-1]
		index+=1
else:
	while(index <= len(C)):
		if(index <= number_People):
			cost = cost + C[index-1]
			heapq.heappush(userHeap, (1, index))
		else:
			nl = userHeap[0]
			cost = cost + ( (nl[0]+1) * C[index-1])
			heapq.heappushpop(userHeap, ( nl[0]+1, nl[1] ))
		index += 1
print(cost)