# Neel Agarwal @Neelka96
# Last Updated: 12.7.2024

# PyPoll Instructions
# In this Challenge, you are tasked with helping a small,
# rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates 
# each of the following values:
# -----------------------------
# *The total number of votes cast       # == total rows in csv
# *A complete list of candidates who received votes     # print list of vote choices
# *The percentage of votes each candidate won
# *The total number of votes each candidate won
# *The winner of the election based on popular vote
# *Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# Candidate dictionary = {"candidate": total votes}
# Access candidate votes through "candidate" key
# --> Candidate vote % = candidate votes / total votes (already tracked) 
# 
# OBJECTIVES:
# (Import modules, init global vars, init lists/dicts)
#   Needs to be able to open files for reading and writing ind. of OS (.path method)
#   Reads CSV file row by row into iterator (with open() --> for loop)
#       Track how many votes were cast --> Increment var w/ each row
#       Create list of different candidates --> Use dict. ("key":value)
#       Use the found key to increment value w/ each vote --> dict["key"] += 1
#   store % of each candidate in new var for accessing later
#   Compare percentages/vote count to find popular vote winner --> If...Else Statement 
# Import necessary modules
import csv
import os
# Set OS dependent paths for in/out files
inPath = os.path.join("Resources", "election_data.csv")
outPath = os.path.join("analysis", "election_analysis.txt")
# GLOBAL VARIABLES:
# -----------------
totalVotes = 0
candidates = {}
# Open CSV for reading & fill in candidate dictionary
with open(inPath, "r") as inData:
    csvReader = csv.reader(inData, delimiter = ',')
    headers = next(csvReader)   # Read headers
    for row in csvReader:
        if row[2] not in candidates:    # If candidate key doesn't exist, create it
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1     # If already exists, increment by 1
        totalVotes += 1     # Incremement vote count with each row
# FINDING WINNER:
# Loop through dictionary and compare vals 
# --> Replace lower vals w/ greater vals in list
# Winner [# votes, candidate] saved, tied counts appended
winner = [0, ""]
for key in candidates:
    # Convert candidate values to list of [# votes, % of total vote]  
    candidates[key] = [candidates[key], (candidates[key]/totalVotes)*100]

    if candidates[key][0] > winner[0]:     # Checks for greatest # votes
        winner[0] = candidates[key][0]
        winner[1] = key
        if len(winner) > 2:     # Deletes tied entries if new greatest # votes found
            del winner[2:]
    elif candidates[key][0] == winner[0]:  # Checks for ties
        winner.append(candidates[key][0])
        winner.append(key)

# Dictionary now looks like:
#   candidates = {"candidate_name": [# votes, % of total vote]}
# PRINTING BLOCK:
# ---------------
outString = "Election Results\n"
outString += f"{'-' * 25}\n"
outString += f"Total Votes: {totalVotes}\n"
outString += f"{'-' * 25}\n"

for key in candidates:
    outString += f"{key}: {(candidates[key][1]):.3f}% ({candidates[key][0]})\n"

outString += f"{'-' * 25}\n"
outString += f"Winner: {winner[1]}\n"
outString += f"{'-' * 25}\n"

print(outString)
# FILE WRITING
with open(outPath, 'w') as outData:
    outData.write(outString)