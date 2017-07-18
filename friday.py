yearArray = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYearArray = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfWeek = [0] * 7
dayOfYear = 13

inputYear = input("How many years since 1900? ")
inputYear = int(inputYear)
year = 1900
#check if year is leap year
def isLeap():
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

#loop to continue adding days until the inputYear is met
while year < 1900 + inputYear:
    if isLeap():
        for num in range(12):
            x = dayOfYear % 7 # Finds the day of week the 13th falls on
            dayOfWeek[x] = dayOfWeek[x] + 1
            dayOfYear = dayOfYear + leapYearArray[num]
    else:
        for num in range(12):
            x = dayOfYear % 7
            dayOfWeek[x] = dayOfWeek[x] + 1
            dayOfYear = dayOfYear + yearArray[num]
    year = year + 1


#36 33 34 33 35 35 34
print(dayOfWeek[6])
print(dayOfWeek[0])
print(dayOfWeek[1])
print(dayOfWeek[2])
print(dayOfWeek[3])
print(dayOfWeek[4])
print(dayOfWeek[5])
