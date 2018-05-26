import os
data_file_name=input("Enter name of the file in Resources folder (Enter for election_data_1.csv): ")
if data_file_name=="":
    data_file_name="election_data_1.csv"
csvpath = os.path.join('Resources', data_file_name)

import csv

poll_outcomes={}

votes_count=0

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    for row in csvreader:
        votes_count=votes_count+1
        
        if row[2] in poll_outcomes:
            poll_outcomes[row[2]]=poll_outcomes[row[2]]+1
        else:
            poll_outcomes[row[2]]=1

        

write_to_file=1
winner=""
winner_count=0
import sys

output_file=data_file_name[:data_file_name.find('.')]+"_results.txt"

while write_to_file>=0:
    if write_to_file==1:
        temp = sys.stdout                 # store original stdout object for later
        sys.stdout = open(os.path.join('Output', output_file ), 'w') # redirect all prints to this log file

    print("Election Results")
    print("------------------")
    print("Total Votes: "+str(votes_count))
    print("------------------")
    for key, value in poll_outcomes.items():
        print(key+": "+str(round(100*value/votes_count,1))+"% ("+str(value)+")")
        if winner_count<value:
            winner_count=value
            winner=key
    
    print("------------------")
    print("Winner: "+winner)
    print("------------------")

    if write_to_file==1:
        sys.stdout.close()                # ordinary file object
        sys.stdout = temp                 # restore print commands to interactive prompt
    
    write_to_file=write_to_file-1







