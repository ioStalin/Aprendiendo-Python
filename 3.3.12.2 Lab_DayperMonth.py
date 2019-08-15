#lab 3.3.12.2 Paremeterized functions
#This function which takes two arguments (a year and a month) and returns
#the number of days for the given month/year pair (yes, we know that only
#February is sensitive to the year value, but we want our function to be
#universal). 

def IsYearLeap(year):
    if (year%4 == 0  and year%100 != 0 or year%400 == 0):
        #print("Leap Year")
        return True
    else:
        #print("NO Leap Year")
        return False

def DaysInMonth(year,month):
    if (IsYearLeap(year) == True):
            if (month>=3 and month<=12 or month ==1):
                if(month<=7):
                    if(month%2==0):
                        print("Month:30 Days")
                        return 30
                    else:
                        print("Month:31 Days")
                        return 31
                else:
                    if(month%2==0):
                        print("Month:31 Days")
                        return 29
                    else:
                        print("Month:30 Days")
                        return 30
            else:
                if(month==2):
                    print("Month:29 Days")
                    return 29
    else:
            if (month>=3 and month<=12 or month ==1):
                if(month<=7):
                    if(month%2==0):
                        print("Month:30 Days")
                        return 30
                    else:
                        print("Month:31 Days")
                        return 31
                else:
                    if(month%2==0):
                        print("Month:31 Days")
                        return 29
                    else:
                        print("Month:30 Days")
                        return 30
            else:
                if(month==2):
                    print("Month:28 Days")
                    return 28

        


testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"->",end="")
	result = DaysInMonth(yr,mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")
