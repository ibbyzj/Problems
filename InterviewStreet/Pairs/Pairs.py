import sys

lineNumber = 1
numberMap = {}
numberList = []
#Runtime is O(n) , one pass to put elements in dictionary and second pass through the array to check for pairs
for line in sys.stdin:
	#Store the number in the second element in list ( difference )
	if(lineNumber == 1):
		firstList = map(int,line.rstrip('\n').split(' '))
	if(lineNumber == 2):
		for each_number in line.rstrip('\n').split(' '):
			numberList.append(int(each_number))
			numberMap[each_number] = int(each_number)
	lineNumber += 1

difference = int(firstList[1])

count = 0

for each_number in numberList:
	if(numberMap.has_key(each_number - difference)):
		count += 1
print(str(count))