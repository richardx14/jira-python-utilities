This utility works out wip from Jira data for each date in a range and shows the max value.

The columns the utility uses are In Progress, Deploying, Deployed, Done.

In does not matter if a story moves across those columns - if it is present in any of them then they are included in the wip count.

It will need to (pseudo code):

- open a csv file
- a dictionary with key = date and value = wip count
- look at each row in the csv, look for date ranges
- for each date in the range, add 1 to the date dictionary for that date
- Do not count anything after the Done date if that is present.

If Done date is blank, from each row:
	Count from In Progess Date to end of date range (e.g. end of month)
	Increment count for each date found
else if Done date is present
	Count from In Progress Date to Done date - 1	 
	Increment count for each date found


Example:

2021-08-25		2021-09-06	
2021-08-17	2021-08-17		
2021-08-10		2021-08-13	
2021-07-30		2021-08-23	
2021-06-29			
2021-08-04			2021-08-04
2021-08-17	2021-08-17	2021-08-17	2021-08-19
2021-08-23		2021-08-24	2021-08-26
2021-08-20			2021-08-26
2021-08-19			2021-08-27
2021-07-21	2021-07-28	2021-07-30	2021-08-02
2021-07-29	2021-07-30	2021-08-09	2021-08-10