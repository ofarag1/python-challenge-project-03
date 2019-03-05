# Dependencies

import os
import csv

# Open and read csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# Skip header

    header = next(csvreader)

# Lists to store data

    month = []
    profit_losses = []
    profit_change = []

# Run through the loop and add them to the lists

    for row in csvreader:
        # Add month
        month.append(row[0])
        # Add profit_losses
        profit_losses.append(int(row[1]))
    
    for i in range(len(profit_losses)-1):
        subtract = profit_losses[i+1]-profit_losses[i]
        # Add profit_change
        profit_change.append(subtract)

# Greatest Increase in Profits & Greatest Increase in Profits

greatest_inc = max(profit_change)
greatest_dec = min(profit_change)

# Greatest Increase Month & Greatest Decrease Month, Month list is 86 and profit_change list is 85. To get the month you have to add 1
 
great_inc_month = month[profit_change.index(max(profit_change))+1]
great_dec_month = month[profit_change.index(min(profit_change))+1]

# Total Month

total_months = len(month)

# Calculate Average Change 

average_change = round(sum(profit_change)/len(profit_change),2)

# Total Profit Losses

total_profit_losses = sum(profit_losses)

# Output 

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{(total_months)}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {great_inc_month} (${(str(greatest_inc))})")
print(f"Greatest Decrease in Profits: {great_dec_month} (${greatest_dec})")

# Set variable for output file

output_file = os.path.join("output", "pybank.txt")

#  Open the output file

with open(output_file, 'w') as text:
    text.writelines('Financial Analysis\n')
    text.writelines('----------------------------' + '\n')
    text.writelines('Total Months: ' + str(total_months) + '\n')
    text.writelines('Total: $' + str(total_profit_losses) + '\n')
    text.writelines('Average Change: $' + str(average_change) + '\n')
    text.writelines('Greatest Increase in Profits: ' + str(great_inc_month) + ' ($' + (str(greatest_inc)) + ')'+ '\n')
    text.writelines('Greatest Decrease in Profits: ' + str(great_dec_month) + ' ($' + (str(greatest_dec)) + ')')