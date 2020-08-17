import os 
import csv

csvpath = os.path.join('Resources','budget_data.csv')

total_months = 0
month_change = []
net_PL_init = 0
average_change_PL = 0
previous = 0
date_max_profit = "" 
date_min_profit = "" 
pl_date = ""
mmp = ""
mml = ""
dates = []

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    
    for x in csvreader:
        total_months += 1
        net_PL_init += int(x[1])
        average_change_PL = int(x[1]) - previous
        month_change.append(average_change_PL)
        dates.append(x[0])
        previous = int(x[1])
       
        max_profit = max(month_change)
        mmp = month_change.index(max_profit)  
            
        min_profit = min(month_change)
        mml = month_change.index(min_profit)
        
        
    average = sum(month_change[1:])/(len(month_change)-1) 
    
date_max_profit = dates[mmp]  
date_min_profit = dates[mml]
    
analysis_path = os.path.join('Analysis', 'Analysis.txt')

with open(analysis_path, 'w') as f:
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Net Profit / Loss: ${net_PL_init}\n")
    f.write(f"Average Change: ${round(average, 2)}\n")
    f.write(f"Greatest Increase in Profit: {date_max_profit} ${max_profit}\n")
    f.write(f"Greatest Decrease in Profit: {date_min_profit} ${min_profit}\n")