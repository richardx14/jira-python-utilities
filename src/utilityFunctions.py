# Utility functions

from datetime import date

fileName = "/Users/richard.holloway/Development/hmrc/jira-to-analytics/dlk-output.csv"

defaultCurrentMonth = "09"

ignoreList = ["DLK-853", "DLK-854", "DLK-893", "DLK-695"]

readyColumn = 4
inProgressColumn = 5
deployingColumn = 6
deployedColumn = 7
doneColumn = 8
labelsColumn = 10
createdColumn = 12
statusColumn = 13

def validRow(row, currentMonth):
            
    if row[0] in ignoreList:
        #print(f"{row[0]} in ignoreList")
        #skippedStories.append(row[0])
        return False
            
    if row[inProgressColumn] == "" and row[deployingColumn] == "" and row[deployedColumn] == "" and row[doneColumn] =="": 
        #print(f"{row[0]} blank row skipped")
        #skippedStories.append(row[0])
        return False
            
        # skip if done ticket in previous month, this can happen if someone has updated commented on a done ticket
        
    if row[doneColumn] != "" and row[doneColumn][-5:-3] != currentMonth:
        #print(f"{row[0]} ticket closed in previous month, row skipped")
        #skippedStories.append(row[0])
        return False
    
    #if row[statusColumn] == "Backlog":
    #    return False
        
    return True

def convertDateFomat(jiraDate):
    year = int(jiraDate[0:4])
    month = int(jiraDate[5:7])
    day = int(jiraDate[-2:])
    
    formattedDate = date(year, month, day)
    
    return(formattedDate)