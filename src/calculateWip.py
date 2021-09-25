# Calculate WIP

import csv
from datetime import date
import statistics
from calendar import monthrange
import utilityFunctions

def updateWipByDay(earliest_date, latest_date):

    for n in range(int(earliest_date), int(latest_date)+1): #don't count last date
        
        if n == 22: print(array[0])

        wipByDay[str(n)] +=1 

def findMaxWip(wipDictionary):
    
    maxWip = 0
    maxWipDay = ""
    
    for n in wipDictionary:
    
        if wipDictionary[n] > maxWip:
        
            maxWip = wipDictionary[n]
        
            maxWipDay = n
    
    maxWipDayAndCount = {}
    
    maxWipDayAndCount[str(maxWipDay)] = maxWip
    
    return maxWipDayAndCount

defaultCurrentMonth = "09"

print(f"Current default month {defaultCurrentMonth}")

currentMonth = input("Enter a month in two digit form, e.g. 08: ")

if currentMonth == "" : currentMonth = defaultCurrentMonth
    
numberOfDaysInMonth = monthrange(2021, int(currentMonth))[1]

fileName = "/Users/richard.holloway/Development/hmrc/jira-to-analytics/dlk-output.csv"

readyColumn = 4
inProgressColumn = 5
deployingColumn = 6
deployedColumn = 7
doneColumn = 8
labelsColumn = 10
createdColumn = 12
statusColumn = 13

skippedStories = []

wipByDay = {}

for n in range(1,numberOfDaysInMonth + 1):
    
    wipByDay[str(n)] = 0

with open(fileName, newline='') as csvfile:
    
    numberOfRows = 0
        
    for line in csvfile.readlines():
        array = line.split(',')
        numberOfRows +=1 
        
        jiraId = array[0]
        
        dateRangeForRow = []

        if array[0] == "ID": # skip header row
            continue
            
        ###########

        if utilityFunctions.validRow(array, currentMonth) == False:
            skippedStories.append(array[0])
            continue
                
        if array[statusColumn].find("To Do") >=0 :            # story moved back so ignore for now.
            skippedStories.append(f"{array[0]} - story on backlog or Ready")
            continue        

        if array[utilityFunctions.inProgressColumn] != "":
            dateRangeForRow.append(array[utilityFunctions.inProgressColumn])
            
        if array[utilityFunctions.deployingColumn] != "":
            dateRangeForRow.append(array[utilityFunctions.deployingColumn])
            
        if array[utilityFunctions.deployedColumn] != "":
            dateRangeForRow.append(array[utilityFunctions.deployedColumn])
            
        if array[utilityFunctions.doneColumn] != "":
            dateRangeForRow.append(array[utilityFunctions.doneColumn])
        
        earliestDate = min(dateRangeForRow)
        latestDate = max(dateRangeForRow)
        
        convertedEarliestDate = utilityFunctions.convertDateFomat(earliestDate)
        convertedLatestDate = utilityFunctions.convertDateFomat(latestDate)
        
        if convertedEarliestDate.month != int(currentMonth):
            wipEarliestDate = "01"
        
        else:
            wipEarliestDate = str(convertedEarliestDate.day)
        
        # if not date in the done column, the story is still open or back on Ready.  Need to figoure out backlog date
        
        if array[utilityFunctions.doneColumn] == "":
            latestWipDate = numberOfDaysInMonth
        
        else:
            latestWipDate = str(convertedLatestDate.day)
            
        #cover the case where a story might have been moved back
        
        if array[utilityFunctions.readyColumn] > latestDate:
            latest
        
        updateWipByDay(wipEarliestDate, latestWipDate)
            
        #print(f"e wip day {wipEarliestDate} l wip day {latestWipDate}")
        

wip = findMaxWip(wipByDay)

print(f"Max wip = {wip}")

print(f"average wip = {statistics.mean(wipByDay.values())}")

#print(skippedStories)
print(wipByDay)