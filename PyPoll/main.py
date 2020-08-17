import os
import csv

csv_polldata = os.path.join("Resources/election_data.csv")

with open(csv_polldata, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    

    votes = {}
    total_votes = 0
    vote_percent = {}
    candidates = []
       
    
    for row in csvreader:
        total_votes += 1 
        i = row[2]
        # is candidate in dictionary if so
        if i in votes:
            votes[i]["Count"] += 1
            votes[i]["Percent"] = votes[i]["Count"] / total_votes
        # is candidate in dictionary if not 
        else:
            votes[i] = {"Count":1}
            votes[i]["Percent"] = votes[i]["Count"] / total_votes
            candidates.append(i)
            
winner = ""
max_votes = 0

for candidate in candidates:
    candidate_votes = votes[candidate]["Count"]
    
    if candidate_votes > max_votes:
        max_votes = candidate_votes
        winner = candidate

analysis_path = os.path.join('Analysis', 'Analysis.txt')

with open(analysis_path, 'w') as f:
    f.write(f"Election Results\n")
    f.write(f"----------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write(f"----------------\n")

    for candidate in candidates:
        votes_percent = votes[candidate]["Percent"] * 100
        votes_count = votes[candidate]["Count"]
        
        f.write(f"{candidate} : {votes_percent:.3f}% ({votes_count})\n")

    f.write(f"----------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"----------------\n")