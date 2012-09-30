#Candies Problem at interviewStreet, I Love Candies :D
#A Good explanation of this can be found out on https://gist.github.com/3440598#comments
N = int(raw_input())
children = candyArray = []
for x in range(0,N):
	cL.append(int(raw_input()))
	candyArray.append(1)
for x in range(0,len(cL)):
	if(x > 0):
		if(children[x-1] < children[x]):
			candyArray[x] = candyArray[x-1]+1
		else:
			j = x
			while(j>0 and (cL[j-1] > cL[j])):
				candyArray[j-1] = max(candyArray[j-1],candyArray[j]+1)
				j -= 1
print(sum(candyArray))





"""
Garbage writing in process...........
import sys
N = int(raw_input())
cL = []

for x in range(0,N):
	cL.append(int(raw_input()))

candyScore = 0
candyCount = 1
decCounter = 0
for x in range(0,len(cL)):
	#First child check
	if(x == 0):
		if(cL[x] > cL[x+1]):
			decCounter += 1
		else:
			candyCount = 1
	elif(x == len(cL)-1):
		if(cL[x] < cL[x-1]):
			candyCount = 1
		elif(cL[x] > cL[x-1]):
			candyCount += 1
		else:
			decCounter += 1
	else:
		if(cL[x] > cL[x-1]):
			candyCount += 1
			decCounter = 0
		elif(cL[x] < cL[x-1] and cL[x] < cL[x+1]):
			if(decCounter != 0):
				decCounter += 1
				candyScore += decCounter
				decCounter = 0
				continue
			else:
				candyCount = 1
				decCounter = 0
				candyScore += candyCount
				continue
		elif(cL[x] < cL[x-1] and cL[x] >= cL[x+1]):
			decCounter += 1
			candyCount = 0
		elif(cL[x] == cL[x-1] and cL[x] <= cL[x+1]):
			candyCount = 1
			decCounter = 0
		elif(cL[x] == cL[x-1] and cL[x] > cL[x+1]):
			if(decCounter != 0):
				decCounter = 0
			candyCount = 0
			decCounter +=1
	if(decCounter > 0):
		candyScore += decCounter
		candyCount = 0
	else:
		candyScore += candyCount
print(candyScore)
"""