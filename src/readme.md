This utility calculates flow metric data from a Jira extract CSV file.  Currently, it calculates max wip over a given month and average flow time.

This has been created as Jupyter notebook initially, althought I have started to move it to a Python package structure.

Flow time is calculated as Done date (if present) - In Progress Date.  Take care if a story has been moved back to a Ready or Backlog queue.  For now if the status is "To Do" or "Backlog", then then the story is skipped.

Wip as calculated as follows.  For each row, an earliest and latest date are determined.  Wip is then stacked by adding 1 to each day in the range between earliest and latest date.   Some rules:

- If a story is not done, then the latest date is the last day of the month.
- If a story started before the current month, then the earliest date is the first day of the month.

The header for a compatible file looks like the below.  This utility only reads the ID, In Progress, Deploying, Deployed, Done columns.

ID	Link	Name	Backlog	Ready	In Progress	Deploying	Deployed	Done	Type	Labels	Updated	Created	Status

Date format is yyyy-mm-dd as a string.

Future enhancements being considered:

- time theft calculations
- Create a format such that charts in Google Sheets can be created without too much cut and pasting
- Count no of days a story spends in each column. 
