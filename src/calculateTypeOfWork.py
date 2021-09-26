# calculate type of work

import csv
from datetime import date
import statistics
import utilityFunctions

defaultCurrentMonth = utilityFunctions.defaultCurrentMonth

print(f"Current default month {defaultCurrentMonth}")

currentMonth = input("Enter a month in two digit form, e.g. 08: ")

if currentMonth == "" : currentMonth = defaultCurrentMonth

fileName = utilityFunctions.fileName

noOfStoriesTouched = 0

unplannedWorkCount = 0
productWorkCount = 0
teamWorkCount = 0

unplannedWork = "unplannedWork"
productWork = "productWork"
teamWork = "teamWork"

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
        
        noOfStoriesTouched += 1
         
        if array[utilityFunctions.labelsColumn].find(unplannedWork) >=0 : 
            unplannedWorkCount += 1
        if array[utilityFunctions.labelsColumn].find(productWork) >= 0 : 
            productWorkCount += 1
        if array[utilityFunctions.labelsColumn].find(teamWork) >= 0 : 
            teamWorkCount += 1
            
print(f"no of stories touched {noOfStoriesTouched} unplannedWork {unplannedWorkCount} productWork {productWorkCount} teamWork {teamWorkCount}")