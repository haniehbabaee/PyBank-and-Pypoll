# Import dependencies
import csv
import os

# Change directory to the directory of current python script
file_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open (file_path, 'r') as input_file:
    csvreader = csv.reader(input_file, delimiter = ",")
    csv_header = next(csvreader)

    # Define Pypoll's variables
    candidate_list=[]
    Total_votes = 0    
    first_sum=0
    second_sum=0
    third_sum=0
    fourth_sum=0

    # Read through each row of data after the header
    for row in csvreader:
        # Count of votes
        Total_votes+=1
        # find the candidates and their votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            if row[2]==candidate_list[0]:
                first_sum +=1
            elif row[2]==candidate_list[1]:
                second_sum +=1
            elif row[2]==candidate_list[2]:
                third_sum +=1
            elif row[2]==candidate_list[3]:
                fourth_sum +=1
        
        elif row[2]==candidate_list[0]:
            first_sum +=1
        elif row[2]==candidate_list[1]:
            second_sum +=1
        elif row[2]==candidate_list[2]:
            third_sum +=1
        elif row[2]==candidate_list[3]:
            fourth_sum +=1

    # find the winner by maximum vote
    sum_list=[first_sum, second_sum, third_sum, fourth_sum]
    winner_vote=max(sum_list)
    winner_index = sum_list.index(winner_vote)
    winner = candidate_list[winner_index]

    # calculating the vote percentages
    first_percentage= round((first_sum / Total_votes)*100, 2)
    second_percentage= round((second_sum / Total_votes)*100, 2)
    third_percentage = round((third_sum / Total_votes)*100, 2)
    fourth_percentage= round((fourth_sum / Total_votes)*100, 2)

    # print the result
    print("Election Results\n-------------------\n")
    print(f"Total Votes: {Total_votes}\n-------------------\n")
    print(f"{candidate_list[0]}: {first_percentage}%  ({first_sum})\n")
    print(f"{candidate_list[1]}: {second_percentage}%  ({second_sum})\n")
    print(f"{candidate_list[2]}: {third_percentage}%  ({third_sum})\n")
    print(f"{candidate_list[3]}: {fourth_percentage}%  ({fourth_sum})\n-------------------\n")
    print(f"Winner: {winner}\n-------------------")

    # Export a text file with the results
    review_file = os.path.join("analysis", "election_data.txt")
    with open(review_file, "w") as outfile:

        outfile.write("Election Results\n-------------------\n")
        outfile.write(f"Total Votes: {Total_votes}\n-------------------\n")
        outfile.write(f"{candidate_list[0]}: {first_percentage}%  ({first_sum})\n")
        outfile.write(f"{candidate_list[1]}: {second_percentage}%  ({second_sum})\n")
        outfile.write(f"{candidate_list[2]}: {third_percentage}%  ({third_sum})\n")
        outfile.write(f"{candidate_list[3]}: {fourth_percentage}%  ({fourth_sum})\n-------------------\n")
        outfile.write(f"Winner: {winner}\n-------------------")
    
   
    

    