"""
Python script for reading lines - Spotify puzzle ( Complicated >.< )
Store all the first branch and second branch employees in two separate dictionaries
Iterate over the first elements taking the second ones count after the first
"""
import sys
import operator

count = 0

#Opening the file and reading line by line
#handle = open('testFile.txt','rb')
project_list = []
number = 0

for line in sys.stdin:
	if count == 0:
		number = int(line.rstrip('\n'))
		count += 1
	else:
		input_line = line.rstrip('\n')
		project_list.append([int(input_line.split(' ')[0]),int(input_line.split(' ')[1])])

#Initialising first branch, second branch and final employee list
first_branch = {}
second_branch = {}
final_employee_list = []
#print "======================================================================"
#print str(number)+" is the number of lines present"
#print "This is unsorted"
#print project_list
#print "======================================================================"

project_list.sort(key = lambda x: x[0])

for each in project_list:
	if first_branch.has_key(each[0]):
		first_branch[each[0]] = first_branch[each[0]]+' '+str(each[1])
	else:
		first_branch[each[0]] = str(each[1])
#print first_branch
#print "======================================================================"

project_list.sort(key = lambda x: x[1])

for each in project_list:
	if second_branch.has_key(each[1]):
		second_branch[each[1]] = second_branch[each[1]]+' '+str(each[0])
	else:
		second_branch[each[1]] = str(each[0])
#print second_branch
#print "======================================================================"
project_list.sort(key = lambda x: x[0])
#print project_list
for each in project_list:
	
	#For the first employee get the group by count for the first employee and for each of his other employee get the count of them with others and take the highest count, remove the respective element from the dictionary
	skipBig = 0
	to_be_added = 0
	
	#print "Checking elements for "+str(each[0])
	if first_branch.has_key(each[0]):
		#print "======================================================================"
		#print "Count of "+str(each[0])+" with other elements is "+str(len(first_branch[each[0]].split(' ')))
		first_element_count = len(first_branch[each[0]].split(' '))
		to_be_added = each[0]
		for each in first_branch[each[0]].split(' '):
			if str(each) in final_employee_list:
				skipBig = 1
				break
			else:
				#print "count of "+str(each)+" with other elements is "+str(len(second_branch[int(each)].split(' ')))
				if second_branch.has_key(int(each)):
					if len(second_branch[int(each)].split(' ')) > first_element_count:
						to_be_added = int(each)
					else:
						continue
		if skipBig == 0:
			#print "First element added is "+str(to_be_added)
			#print "======================================================================"
			final_employee_list.append(str(to_be_added))
			if first_branch.has_key(to_be_added):
				del first_branch[to_be_added]
			if second_branch.has_key(to_be_added):
				del second_branch[to_be_added]
		else:
			continue
	else:
		#print "======================================================================"
		continue
print float(len(final_employee_list))
for each_element in final_employee_list:
	print each_element