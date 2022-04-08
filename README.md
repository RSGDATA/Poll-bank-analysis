# Python_Challenge

All output for PyPoll and PyBank will be in their respective resources folders. 

Directions:

First click on Either the Finanial Analysis file (PyBank) or Poll Analysis file (PyPoll). Once clicked, you will see a resources folder. 
All content from the analysis will be found in the resources folder, both in the Finanial Analysis file, or the Poll Analysis file.

In each resources folders you will see:

1. Main script "main.py" My script that cleans given data
2. Txtfiles presenting output
3. Screenshot of script printing to the terminal in VS Code
4. CSV files containing source material, in which the analysis is based

The line: 

with open("election_data.csv", 'r') as csvfile: or with open("budget_data.csv", 'r') as csvfile:

Must have the CSV file in the same folder as the main script.
If the CSV file is in a seperate folder from the main script you will have to the write in the file name with a slash to access the csv.

Example of altered with open line:

with open("resources/election_data.csv", 'r')

I advise putting the CSV file in the same folder as the main script, so no changes need to be made for the progam to run.



Poll Analysis:

The source material comes from a CSV file contanining 3 columns, and nearly 37,000 rows. 1st column contains Ballot ID (Header: Ballot ID),
2nd contains county in which the voting took place (Header: County) and 3rd column has Candidate names (Header: Candidate)

Program Output:

1. Totals the rows ( in this case it's votes )

2. Populates a dictionary with keys based on names in the third column, and lists containing the percentage of, and count of values in the first two columns
   adjacent to the third column Keys. Conditionals are set in place before the dictionary is filled, so that the output shows each candidates name, followed
   by percenentage of the votes that each candidate recieved, followed by the vote count.

3. Lastly a Key with the greatest value is shown at the end. This is shown as Winner. 
  
  


PyBank Analysis:

The source material comes from a CSV file containing two columns, and 86 rows. 1st column contains months and day.
2nd column contains the profit and loss for each month and date.

Program Output:

1. Totals the rows ( in this case months )

2. Populates net total amount of "Profit/Losses" over the entire period: This is done by incrementing down both rows using loops and conditonals.
   This process takes all of the positive and negative revenue, and subtracts the current row that is being incremented from the last row that was previously 
   incremented. In this case it results in a positive number at the end of the 86 months. 

3. Shows average change: This is achieved by variable "change" taking on the value of "total_change" variable. Then "total_change" is divided by "total_months"
   and the quotient is store in new variable "average_change" after this process is fully incremented through all 86 rows the result shows the average change in 
   in revenue for any given month. This happens to be a negative number in this case.

4. The last two line displays the months that have the greatest increase and greatest decrease in profits: This is done by again using "change" variable 
   in an If statement, to gather the positive or negative change and to store the results in the max_value and max_date, and min_value and min_date. 






   










