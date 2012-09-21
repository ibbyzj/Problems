#Python file for interview street median problem ( passes 7 cases )
from __future__ import division
import math
import sys
import heapq
from decimal import Decimal
#Python supports only min heaps in the heapq module >.< , entering negative values in the left heap.
        
def heapElement(leftHeap,rightHeap):
		#Check if the heaps are balanced
		if(len(leftHeap) == 0 and len(rightHeap) == 0):
			return("Wrong!")
		elif(len(rightHeap)==0):
			return(Decimal(leftHeap[0]*(-1)))
		elif(len(leftHeap) > len(rightHeap)):
			return(Decimal((-1)*leftHeap[0]))
		else:
			if ( (leftHeap[0]*(-1) > 9223372036854775807) or rightHeap[0]>9223372036854775807 or (leftHeap[0]*(-1) < -9223372036854775807) or rightHeap[0]<-9223372036854775807):
				sum = Decimal(Decimal(leftHeap[0]*(-1)) + Decimal(rightHeap[0]))
				doIt = Decimal(Decimal(sum)/2)
				if((sum % 2) == 0):
					return (Decimal(doIt))
				else:
					return Decimal(doIt)
			else:
				sum = ((leftHeap[0]*(-1)) + (rightHeap[0]))
				doIt = Decimal(Decimal(sum)/2)
				if((sum % 2) == 0):
					return (int(doIt))
				else:
					return (doIt)


#Max heap on the left
leftHeap = []
#Min heap on the right
rightHeap = []
N = int(raw_input())

for i in range(0, N):
	temp = raw_input()
	a, b = [xx for xx in temp.split(' ')]
	number = int(b)
	if(a == 'a'):
		#Adding numbers to the heap is fairly simple
		if(len(leftHeap) == len(rightHeap)):
			if(len(rightHeap) == 0):
				heapq.heappush(leftHeap,-number)
			elif(number > rightHeap[0]):
				heapq.heappush(leftHeap,-(heapq.heappushpop(rightHeap,number)))
			else:
				heapq.heappush(leftHeap,-number)
		else:
			if(number < (leftHeap[0]*(-1))):
				heapq.heappush(rightHeap,(heapq.heappushpop(leftHeap,-number)*(-1)))
			else:
				heapq.heappush(rightHeap,number)
		print(heapElement(leftHeap,rightHeap))
	else:
		#Check if the element exists in both the heaps
		leftExists = True
		rightExists = True
		try:
			removeIndex = leftHeap.index(-number)
		except:
			leftExists = False
		if(leftExists == True):
			leftHeap[removeIndex] = leftHeap[-1]
			leftHeap.pop()
			try:
				heapq._siftup(leftHeap,removeIndex)
			except:
				heapq.heapify(leftHeap)
		if(leftExists == False):
			try:
				removeIndex = rightHeap.index(number)
			except:
				rightExists = False
			if(rightExists == True):
				rightHeap[removeIndex] = rightHeap[-1]
				rightHeap.pop()
				try:
					heapq._siftup(rightHeap,removeIndex)
				except:
					heapq.heapify(rightHeap)
		#Python siftup heap function removes the element in log(n) rather than O(n)
		if(leftExists == False and rightExists == False):
			print("Wrong!")
			continue
		else:
			if(len(leftHeap) < len(rightHeap)):
				heapq.heappush(leftHeap,-(heapq.heappop(rightHeap)))
			if(len(leftHeap) > len(rightHeap)+1):
				heapq.heappush(rightHeap,-(heapq.heappop(leftHeap)))
		print(heapElement(leftHeap,rightHeap))