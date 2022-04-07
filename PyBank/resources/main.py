import csv
import math


w = open("PyBank.txt", "w")

total_profit_losses = 0
current = 0
last = 0
max_value = 0
max_date = 0
total_change = 0
months = 0
min_value = 0
min_date = 0

with open("resources/budget_data.csv", 'r') as csvfile:

  data = []



  csvreader = csv.reader(csvfile, delimiter=',')


  csv_header = next(csvreader)



# loop through all of the rows in the csv
  for row in csvreader:
    data.append(row)

    total_profit_losses = total_profit_losses + int(row[1])
    

    months = months + 1
    
    

    current = int(row[1])
    
    

    if months > 1:
      change = current - last
      
      #If the ammount is more than it was previuosly
      if change > max_value:
        max_value = change
        max_date = row[0]
        
      #If the ammount is less than it was before 
      if change < min_value:
        min_value = change
        min_date = row[0]
        
   

      total_change = total_change + change
    
    
    


      average_change = total_change / (months - 1)
    
    # Sets current row to last row before next loop begins. Current row is now one row ahead of last row.
    last = int(row[1])
    
  
  Two_Dec = "{:.2f}".format(average_change)

  print("Financial Analysis")
  w.write("Financial Analysis"+ "\n")

  print("-----------------------")
  w.write("-----------------------\n")


  print("Total Months:", len(data))
  w.write("Total Months: " + str(len(data))+ "\n")
  
  print("Total:" + " $" + str(total_profit_losses))
  w.write("Total:" + " $" + str(total_profit_losses) + "\n")
  
  
  print("Average Change:"+ " $" + str( Two_Dec ))
  w.write("Average Change:"+ " $" + str(Two_Dec)+ "\n")
  
  print("Greatest Increase In Profits:", max_date, "(" + str("$" + str(max_value) + ")"))
  w.write("Greatest Increase In Profits:"+ max_date + "(" + str("$" + str(max_value) + ")")+"\n")
  
  print("Greatest Drecrease In profits:",min_date,"("+str("$" + str(min_value)+")"))
  w.write("Greatest Drecrease In profits:" + min_date + "("+str("$" + str(min_value)+")")+"\n")

  w.close()