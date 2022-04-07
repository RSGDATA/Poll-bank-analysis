import csv
import os
 
w = open("PyPoll.txt", "w")

candidates = {}


total_votes = 0

most_ballot_count = 0
most_candidate_name = ""

rowcount = -1


with open("election_data.csv", 'r') as csvfile:

    data = []

 
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)

    

    
    print("Election Results")
    w.write("Election Results\n")
    
    print("---------------")
    w.write("--------------\n")

    for row in csvreader:
        data.append(row)
        candidate_type = row[2]

        total_vote = total_votes + 1
        


        if candidate_type in candidates:
            candidates[candidate_type] = candidates[candidate_type] + 1
        else:
     
            
            candidates[candidate_type] = 1
    
    print("Total Votes:", len(data))
    w.write("Total Votes:" + str(len(data))+ "\n")
    print("----------------")
    w.write("----------------\n")
    for key, value in candidates.items():

        if value > most_ballot_count:
            most_candidate_name = key
            most_ballot_count = value

    
        output = key+ ": " + " " + str(round(value / len(data) * 100,3)) + "% (" + str(value) + ")" 
        print(output)
        w.write(output + "\n")

    print("-----------------")
    w.write("----------------- \n")
    print("Winner " + most_candidate_name)
    w.write("Winner " + most_candidate_name + "\n")

    w.close()


        

        
        
     
      
      
        














