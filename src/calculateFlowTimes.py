# Calculate Flow Times

import csv
from datetime import date
import statistics
import utilityFunctions

def validRow(row):
            
    if row[0] in utilityFunctions.ignoreList:
        #print(f"{row[0]} in ignoreList")
        return False
            
    if row[inProgressColumn] == "" and row[deployingColumn] == "" and row[deployedColumn] == "" and row[doneColumn] =="": 
        #print(f"{row[0]} blank row skipped")
        return False
            
        # skip if done ticket in previous month, this can happen if someone has updated commented on a done ticket
        
    if row[doneColumn] != "" and row[doneColumn][-5:-3] != currentMonth:
        #print(f"{row[0]} ticket closed in previous month, row skipped")
        return False
    
    return True

def convertDateFomat(jiraDate):
    year = int(jiraDate[0:4])
    month = int(jiraDate[5:7])
    day = int(jiraDate[-2:])
    
    formattedDate = date(year, month, day)
    
    return(formattedDate)

def calculateFlowTime(startDate, endDate):
    
    fdate = date(int(startDate[0:4]),int(startDate[5:7]),int(startDate[-2:]))
    
    ldate = date(int(endDate[0:4]),int(endDate[5:7]),int(endDate[-2:]))

    delta = ldate - fdate

    print(f"start date {fdate} done date{ldate} flow time {delta.days}")
    
    return(delta.days)

#################################

defaultCurrentMonth = "09"

print(f"Current default month {defaultCurrentMonth}")

currentMonth = input("Enter a month in two digit form, e.g. 09: ")

if currentMonth == "" : currentMonth = defaultCurrentMonth

flowTimes = []

fileName = "/Users/richard.holloway/Development/hmrc/jira-to-analytics/dlk-output.csv"

inProgressColumn = 5
deployingColumn = 6
deployedColumn = 7
doneColumn = 8
labelsColumn = 10
createdColumn = 12
statusColumn = 13

skippedStories = []

with open(fileName, newline='') as csvfile:
    
    numberOfRows = 0
        
    for line in csvfile.readlines():
        array = line.split(',')
        numberOfRows +=1 
        
        jiraId = array[0]
        
        dateRangeForRow = []

        if array[0] == "ID": # skip header row
            continue

        if validRow(array) == False:
            skippedStories.append(array[0])
            continue
        
        if array[statusColumn] == "To Do" or array[statusColumn] == "Backlog":
            # story moved back so ignore for now.
            skippedStories.append[f"{array[0]} - story on backlog or Ready"]
            continue
        
        if array[inProgressColumn] != "":
            dateRangeForRow.append(array[inProgressColumn])
            
        if array[deployingColumn] != "":
            dateRangeForRow.append(array[deployingColumn])
            
        if array[deployedColumn] != "":
            dateRangeForRow.append(array[deployedColumn])
            
        if array[doneColumn] != "":
            dateRangeForRow.append(array[doneColumn])
        
        earliestDate = min(dateRangeForRow)
        latestDate = max(dateRangeForRow)
        
        convertedEarliestDate = convertDateFomat(earliestDate)
        convertedLatestDate = convertDateFomat(latestDate)
        
        delta = convertedLatestDate - convertedEarliestDate
        
        if array[doneColumn] != "":
            
            flowTime = delta.days
            
            flowTimes.append(flowTime)
        
            print(f"{jiraId} earliest date {earliestDate}, latest date {latestDate}, flowTime = {flowTime}, labels = {array[labelsColumn]}")
        
        else:
            
            print(f"{jiraId} earliest date {earliestDate}, latest date {latestDate}, labels = {array[labelsColumn]}")
        
print()
print(f"skippedStories {skippedStories}")

print()
print(f"average flow time = {statistics.mean(flowTimes)}")        
print(f"stdev flow time = {statistics.stdev(flowTimes)}")
print()
