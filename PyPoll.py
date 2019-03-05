# Dependencies

import os
import csv
import operator

csvpath = os.path.join('Resources', 'election_data.csv')

# Open and read csv

with open(csvpath, newline ="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')

# Skip header

    header = next(csvreader)

    voters_num = []
    candidate = []

# Number of voters

    for row in csvreader:
        voters_num.append(row[0])
        candidate.append(row[2])

# Total number of winners

total_num_votes = len(voters_num)

# Count number of Candiates

khan_num_votes = candidate.count('Khan')

correy_num_votes = candidate.count('Correy')

li_num_votes = candidate.count('Li')

oTooley_num_votes = candidate.count("O'Tooley")

# Calculate the percetange of each candidate

khan_per = round((khan_num_votes/(total_num_votes))*100, 4)

correy_per = round((correy_num_votes/(total_num_votes))*100, 4)

li_per = round((li_num_votes/(total_num_votes))*100, 4)

oTooley_per = round((oTooley_num_votes/(total_num_votes))*100, 4)

# Add two list in one dictionary to determine the winner

candidates_winner = ["Khan", "Correy", "Li","O'Tooley"]

votes_winner = [khan_num_votes,correy_num_votes,li_num_votes,oTooley_num_votes]

dict = dict(zip(candidates_winner, votes_winner))

winner = max(dict.items(), key=operator.itemgetter(1))[0]

# Print the summary table

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_num_votes}")
print(f"-------------------------")
print(f"Khan: {khan_per:.3f}% ({khan_num_votes})")
print(f"Correy: {correy_per:.3f}% ({correy_num_votes})")
print(f"Li: {li_per:.3f}% ({li_num_votes})")
print(f"O'Tooley: {oTooley_per:.3f}% ({oTooley_num_votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Set variable for output file

output_file = os.path.join("output", "pypoll.txt")

#  Open the output file

with open(output_file, 'w') as text:
    text.writelines('Election Results\n')
    text.writelines('-------------------------' + '\n')
    text.writelines('Total Votes: ' + str(total_num_votes) + '\n')
    text.writelines('-------------------------' + '\n')
    text.writelines(f"Khan: {khan_per:.3f}% ({khan_num_votes})" + '\n')
    text.writelines(f"Correy: {correy_per:.3f}% ({correy_num_votes})" + '\n')
    text.writelines(f"Li: {li_per:.3f}% ({li_num_votes})" + '\n')
    text.writelines(f"O'Tooley: {oTooley_per:.3f}% ({oTooley_num_votes})" + '\n')
    text.writelines('-------------------------' + '\n')
    text.writelines('Winner: ' + str(winner) + '\n')
    text.writelines('-------------------------' + '\n')


