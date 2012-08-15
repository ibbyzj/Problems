"""
Python script for first date program, spotify puzzle
Input is the date and output is the least date possible of all the combinations
"""
import sys
import itertools
import time
import datetime

#Function to check if the numbers of days for the given month in date are correct ( also does the leap year check)
def MMandDDCheck(date,isLeap):
	month = int(date[0])
	day = int(float(date[1]))
	
	#Check if month has more than 31 days/ check not needed though, more than 31 days already eliminated....
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day>31):
			return False
	
	#Check on february depending on isLeap parameter
	if month == 2 :
		if isLeap == True:
			if day > 29:
				return False
		else:
			if day > 28:
				return False
	
	#Check on months with no more than 30 days
	if (month == 4 or month == 6 or month == 9 or month == 11) and (day > 30):
		return False
	return True
			
#Function to check validity of date, if months, days and years are valid do individual month checks via the above function
def dateValidity(date):
	
	isLeap = True
	month, day = int(date[0]), int(date[1])
	
	#Checks to ensure month and day are in the right range
	if month > 12 or month < 1 or day > 31 or day < 1:
		return False
	year = date[2]
	if len(year) == 1:
		year = '200'+year
	if len(year) == 2:
		year = '20'+year
	if len(year) == 3:
		year = '2'+year	
	
	year = int(year)
	
	#Year Validity check and Leap year check, the date is then passed to days in month check to the above function ( April cannot have 31 days! )
	if year > 2999 or year < 2000:
		return False
	
	if (year%4 == 0) or (year%100 == 0 and year%400 != 0):
		isLeap = True
		if MMandDDCheck([date[0],date[1]],isLeap) == False:
			return False
		else:
			formatted_date = str(year)+'-'+str(date[0])+'-'+str(date[1])
			return formatted_date
	else:
		isLeap = False
		if MMandDDCheck([date[0],date[1]],isLeap) == False:
			return False
		else:
			formatted_date = str(year)+'-'+str(date[0])+'-'+str(date[1])
			return formatted_date
	

date = raw_input("Enter the Date: ")
newd = date.split('/')

#First generate all the permutations of the date to get the possibilities
permuted = list(itertools.permutations(newd))
dates = []

#Iterate over the list combinations, add the date to the new list if it is a valid date
for each_date in permuted:
	if dateValidity(each_date)==False:
		continue
	else:
	 	new_Date = dateValidity(each_date)
	 	dates.append(new_Date)

#Get the dates and remove the duplicates added
dates = list(set(dates))

dodoDates = []

#Create a datetime list for easier sorting if required
for each_date in dates:
	dodoDates.append(datetime.date(int(each_date.split('-')[0]),int(each_date.split('-')[1]),int(each_date.split('-')[2])))
	
dates = []

#If no dates obtained then the given date is illegal
if len(dodoDates) == 0:
	print date+" is illegal"
	sys.exit()
	
#If only one date is obtained then display it
if len(dodoDates) == 1:
	print dodoDates[0]
	sys.exit()

#If multiple dates are present use the date time min function to ge the minimum date
print min(dodoDates)