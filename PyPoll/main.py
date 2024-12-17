# Neel Agarwal @Neelka96
# Last Updated: 12.7.2024
# PyPoll main.py Script

def AnalyzePollCSV(inStream):   # Args: <str>
    # Reads in .csv file, counts total votes (rows)
    # Creates dict. of "Candidate Name: Votes for that candidate
    # Calls f(x) passing in votes & dict. --> returns mod'd dict. and winner(s) by popular vote
    # Pass along total votes, new candidate dict., and winner(s) to next f(x)
    votes = 0
    candidates = {}
    with open(inStream, "r") as inData:
        csvReader = csv.reader(inData, delimiter = ',')
        headers = next(csvReader)               # Read headers
        for row in csvReader:
            if row[2] not in candidates:        # If candidate name (key) doesn't exist, create it and set to 1
                candidates[row[2]] = 1
            else:
                candidates[row[2]] += 1         # If candidate already exists, increment by 1
            votes += 1                          # Incremement vote count with each row
        # Retrieve modified version of candidate dictionary to pass to formatter and popular vote winner(s)
        candidates, winner = Mod_Dict_Find_Winner(votes, candidates)
    return votes, candidates, winner            # Output analysis summary values (votes, candidate dictionary)

def Mod_Dict_Find_Winner(votes, candidates):    # Args: <int>, <dict obj>
    if ((votes == 0) or (not candidates)):      # !!!Data validation!!!
        print("Error: Invalid data held in CSV file.")
        return {}, ["No Winner", -1]
    # Uses loop to modify dictionary values to include % of votes, then find winner of election
    # If there is a tie, append to winner list: [candidate, votes, candidate, votes, etc...]
    winner = ["", 0]
    for key in candidates:
        # Convert candidate dictionary int value into list of [# votes, % of total vote]  
        candidates[key] = [candidates[key], (candidates[key]/votes)*100]
        if candidates[key][0] > winner[1]:      # Checks for greatest # votes
            winner = [key, candidates[key][0]]
            if len(winner) > 2:                 # Deletes tied entries if new greatest # votes found
                del winner[2:]
        elif candidates[key][0] == winner[1]:   # Checks for ties
            if winner[1] == 0:
                winner = [key, candidates[key][0]]
            else:
                winner += [key, candidates[key][0]]
    return candidates, winner                   # Returns mod'd dict. {"candidate": [vote, % total vote]}, and winner[]

def FormatOutput(votes, candidates, winner):    # Args: <int>, <dict. obj.>, <list obj.>
    # Combine all resultant output into continuously concatenating string variable
    outString = "\nElection Results\n"
    outString += f"{'-' * 25}\n"
    outString += f"Total Votes: {votes}\n"
    outString += f"{'-' * 25}\n"
    for key in candidates:
        outString += f"{key}: {(candidates[key][1]):.3f}% ({candidates[key][0]})\n"
    outString += f"{'-' * 25}\n"
    # Checks for multiple winner names then concatenates
    if len(winner) == 2:
        outString += f"Winner: {winner[0]}"
    else:                   
        outString += "* Winner is tied - Recount or repolling required! *\n"
        outString += "Winners:"
        for index in range(int(len(winner) / 2)):   # Prints any # of winners in correct format
            if index < (len(winner) / 2) - 1:
                outString += f" {winner[index*2]},"
            else:
                outString += f" {winner[index*2]}"
    outString += f"\n{'-' * 25}\n"
    return outString

def SaveOutput(saveContent, outStream):         # Args: <str>, <str>
    # Saving formatted string to path: /PyPoll/analysis/election_analysis.txt
    with open(outStream, 'w') as outData:
        outData.write(saveContent)
    return None


def main():
    # Main Body: Tasks can be read in pseudocode-esque view
    # Set OS independent paths for in/out files
    inPath = os.path.join("Resources", "election_data.csv")
    outPath = os.path.join("analysis", "election_analysis.txt")
    analysisData = AnalyzePollCSV(inPath)
    formattedData = FormatOutput(*analysisData)
    print(f"\n{formattedData}")
    SaveOutput(formattedData, outPath)
    return 0

if __name__ == "__main__":
    # Increasing modularity of main.py with cond'l
    # Import dependent libraries only when main.py is executed
    import os, csv      # Setting inside cond'l keeps libraries in global scope
    main()              # Calling main() sets tasks in motion