#lab 3.3.12.1 Paremeterized functions
#This code permit verify if data into the list are year leap
#To verify it, this code use  two lists - one with the test data,
#and the other containing the expected results. The code will tell
#you if any of your results are invalid.

def IsYearLeap(year):
    if (year%4 == 0  and year%100 != 0 or year%400 == 0):
        #print("Leap Year")
        return True
    else:
        #print("NO Leap Year")
        return False
    
testdata = [1900, 2000, 2016, 1987,2019,2020]
testresults = [False, True, True, False,False,True]
for i in range(len(testdata)):
	yr = testdata[i]
	print(yr,"->",end="")
	result = IsYearLeap(yr)
	if result == testresults[i]:
		print("OK")     #Result is equal to list <testresults> 
	else:
		print("Failed") 
