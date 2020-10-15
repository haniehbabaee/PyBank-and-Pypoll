# Import dependencies
import csv
import os

# Change directory to the directory of current python script
file_path = os.path.join("Resources", "budget_data.csv")
# Open and read csv
with open (file_path, newline="") as input_file:

    csvreader = csv.reader(input_file, delimiter = ",")
    csv_header = next(csvreader)
    
    # Define PyBank's variables
    Total_Months=0
    netchange_list=[]
    month_list=[]
    x=0
    Total=0

    # Read through each row of data after the header
    for row in csvreader:
        # Count of months
        Total_Months+=1
        if x != 0:
            net_change= int(row[1])-x
            netchange_list.append(net_change)
            month_list.append(row[0])
        # Make the value of previous profit row to be equal to current profit row
        x=int(row[1])
        #total and average of the changes in "Profit/Losses" over the entire period 
        Total += int(row[1])
    monthly_average = round(sum(netchange_list)/len(netchange_list),2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    high_profitvalue=max(netchange_list) 
    low_profitvalue=min(netchange_list)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    best_month_index = netchange_list.index(high_profitvalue)
    worst_month_index = netchange_list.index(low_profitvalue)

    # Assign best and worst month
    best_month = month_list[best_month_index]
    worst_month = month_list[worst_month_index]

    # Print the analysis to the terminal
    print("Financial Analysis\n--------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${monthly_average}")
    print(f"Greatest Increase in Profits: {best_month} (${high_profitvalue})")
    print(f"Greatest Decrease in Profits: {worst_month} (${low_profitvalue})")
  
    #  Export a text file with the results
    review_file = os.path.join("analysis", "budget_data.txt")
    with open(review_file, "w") as outfile:

        outfile.write("Financial Analysis\n--------------------\n")
        outfile.write(f"Total Months: {Total_Months}\n")
        outfile.write(f"Total: ${Total}\n")
        outfile.write(f"Average Change: ${monthly_average}\n")
        outfile.write(f"Greatest Increase in Profits: {best_month} (${high_profitvalue})\n")
        outfile.write(f"Greatest Decrease in Profits: {worst_month} (${low_profitvalue})\n")
    