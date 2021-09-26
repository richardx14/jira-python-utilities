# Calculate Flow Times

import csv
from datetime import date
import statistics
import utilityFunctions

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

        if utilityFunctions.validRow(array, currentMonth) == False:
            skippedStories.append(array[0])
            continue
        
        if array[utilityFunctions.statusColumn] == "To Do" or array[utilityFunctions.statusColumn] == "Backlog":
            # story moved back so ignore for now.
            skippedStories.append[f"{array[0]} - story on backlog or Ready"]
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
        
        delta = convertedLatestDate - convertedEarliestDate
        
        if array[utilityFunctions.doneColumn] != "":
            
            flowTime = delta.days
            
            flowTimes.append(flowTime)
        
            print(f"{jiraId} earliest date {earliestDate}, latest date {latestDate}, flowTime = {flowTime}, labels = {array[utilityFunctions.labelsColumn]}")
        
        else:
            
            print(f"{jiraId} earliest date {earliestDate}, latest date {latestDate}, labels = {array[utilityFunctions.labelsColumn]}")
        
print()
print(f"skippedStories {skippedStories}")

print()
print(f"average flow time = {statistics.mean(flowTimes)}")        
print(f"stdev flow time = {statistics.stdev(flowTimes)}")
print()
