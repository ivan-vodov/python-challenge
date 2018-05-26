import os
data_file_name=input("Enter name of the file in Resources folder (Enter for budget_data_1.csv): ")
if data_file_name=="":
    data_file_name="budget_data_1.csv"
csvpath = os.path.join('Resources', data_file_name)

import csv

prev_revenue=0
total_revenue_change=0
revenue_data={"Total Months":0, "Total Revenue":0, "Average Revenue Change":0,"Greatest Increase":["",0],"Greatest Decrease":["",0]}

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    found=False


    
    for row in csvreader:
        revenue_data["Total Months"]=revenue_data["Total Months"]+1

        
        revenue_data["Total Revenue"]=revenue_data["Total Revenue"]+int(row[1])

        if(revenue_data["Total Months"]!=1):
            revenue_change=int(row[1])-prev_revenue
            total_revenue_change=total_revenue_change+revenue_change

            
            if revenue_data["Greatest Increase"][1]<revenue_change:
                revenue_data["Greatest Increase"][1]=revenue_change
                revenue_data["Greatest Increase"][0]=row[0]
            
            
            if revenue_data["Greatest Decrease"][1]>revenue_change:
                revenue_data["Greatest Decrease"][1]=revenue_change
                revenue_data["Greatest Decrease"][0]=row[0]

        prev_revenue=int(row[1])

revenue_data["Average Revenue Change"]=round(total_revenue_change/(revenue_data["Total Months"]-1))


write_to_file=1
import sys
output_file=data_file_name[:data_file_name.find('.')]+"_results.txt"

while write_to_file>=0:
    if write_to_file==1:
        temp = sys.stdout                 # store original stdout object for later
        sys.stdout = open(os.path.join('Output', output_file), 'w') # redirect all prints to this log file

    print("Financial Analysis")
    print("------------------")
    print("Total Months: "+str(revenue_data["Total Months"]))
    print("Total Revenue: $"+str(revenue_data["Total Revenue"]))
    print("Average Revenue Change: $"+str(revenue_data["Average Revenue Change"]))
    print("Greatest Increase in Revenue: "+revenue_data["Greatest Increase"][0]+" ($"+str(revenue_data["Greatest Increase"][1])+")")
    print("Greatest Decrease in Revenue: "+revenue_data["Greatest Decrease"][0]+" ($"+str(revenue_data["Greatest Decrease"][1])+")")
    
    if write_to_file==1:
        sys.stdout.close()                # ordinary file object
        sys.stdout = temp                 # restore print commands to interactive prompt
    
    write_to_file=write_to_file-1







