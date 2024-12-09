# Neel Agarwal @Neelka96
# Last Updated: 12.7.2024
# PyBank main.py Script

def AnalyzeBudgetCSV(inStream):
    # Used for reading the .csv and generating a summary of the budget
    # inStream == OS independent path for reading file
    totalMonths = 0    # Init total months for incrementing
    netProfit = 0      # Init total P&L for continual summing
    changeList = []    # changeList will collect differentials between neighboring values
    dateList = []      # dateList will store the date for the corresponding changeValue
    # changeList <--> dateList relate via corresponding index
    # Open csv path var and begin reading
    with open(inStream, 'r') as inFile:                         # Using "with" for file management (aka context) and file alias
        csvReader = csv.reader(inFile, delimiter = ",")         # Create csv reader object to iterate row to row
        header = next(csvReader)                                # Skip headers
        priorRow = next(csvReader)                              # priorRow init with csv row 1 (used in for loop to gen differentials), exclude in "for" loop
        priorRow[1] = int(priorRow[1])                          # Recast for permanent int usage
        netProfit += priorRow[1]                                # Add current P&L into total
        totalMonths += 1                                        # Incrememnt total months with csv row 1
        # Creating the List of budget changes
        for row in csvReader:
            row[1] = int(row[1])                                # Recast for permanent int usage
            netProfit += row[1]                                 # Calculate total P&L
            totalMonths += 1                                    # Increment months for each row
            budgetChg = row[1] - priorRow[1]                    # Calculate current budget differential from previous budget
            priorRow = row                                      # Reset priorRow to the current row iterable for next loop
            dateList.append(row[0])                             # Appends current date to dateList
            changeList.append(budgetChg)                        # Appends differential to changeList
        # For loop complete --> Begin preparing summary values for export
        avgChg = format(sum(changeList)/len(changeList), ".2f")
        maxVal = MultipleExtremes(dateList, changeList, "max")  # Records all extremities in budget to a max and min lists [date, value, date, value, etc...]
        minVal = MultipleExtremes(dateList, changeList, "min")  # Number of records are irrelevant, later f(x) expects any # of input
    return totalMonths, netProfit, avgChg, maxVal, minVal

def FormatOutput(months, profits, average, maximum, minimum):
    # Function to format output for both terminal and for saving to a file
    # Method is to continuously concatenate string variable that will be returned
    outString = "Financial Analysis\n"
    outString += f"{'-' * 25}\n"
    outString += f"Total Months: {months}\n"
    outString += f"Total: ${profits}\n"
    outString += f"Average Change: ${average}\n"
    # Conditional string editing - check if there are multiple lines that need concatenating
    if len(maximum) == 2:       # Block 1: con. maximum values
        outString += f"Greatest Increase in Profits: {maximum[0]} (${maximum[1]})\n"
    else:
        for n in range(int(len(maximum) / 2)):
            outString += f"Greatest Increase in Profits: {maximum[n*2]} (${maximum[(n*2)+1]})\n"
    if len(minimum) == 2:       # Block 2: con. minimum values
        outString += f"Greatest Decrease in Profits: {minimum[0]} (${minimum[1]})\n"
    else:
        for n in range(int(len(minimum) / 2)):
            outString += f"Greatest Decrease in Profits: {minimum[n*2]} (${minimum[(n*2)+1]})\n"
    return outString    

def SaveOutput(saveContent, outStream):
    # Function to export/save formatted output to a .txt file, path > PyBank/analysis/budget_analysis.txt
    with open(outStream, 'w') as outData:
        outData.write(saveContent)
    return None                 # Personal preference to return void/null for no actual return value

def MultipleExtremes(dates, values, max_or_min):
    # Args: <list of strings>, <list of integers>, <string>
    trueExtreme = None          # Not needed init of trueExtreme (if...else block doesn't localize inits)
    if max_or_min == "max":     # Finding max or the min
        trueExtreme = max(values)
    elif max_or_min == "min":
        trueExtreme = min(values)
    else:
        quit(f"Source code: <max_or_min> arg '{max_or_min}' not valid")
    # Building index list where other matching extremities are found (if they exist)
    otherExtremes = [index for index, extreme in enumerate(values) if extreme == trueExtreme]   # [unpacks enumeration() --> checks if value matches extremity --> stores the index]
    outputExtremes = []         # Create list for output in the format of [data, value] or [date, value, date, value, etc...]
    for index in otherExtremes: # Loop through list of indeces that correspond to dates where a matching max/min was found
        outputExtremes.append(dates[index])
        outputExtremes.append(trueExtreme)
    return outputExtremes

def main():
    # Program Body - provides psuedocode-esque view of method purpose
    inPath = os.path.join("Resources", "budget_data.csv")   # Sets in/out paths
    outPath = os.path.join("analysis", "budget_analysis.txt")
    budgetSummary = AnalyzeBudgetCSV(inPath)                # Read, summarize, and save analysis as a tuple object
    formatSummary = FormatOutput(*budgetSummary)            # '*' Unpacks returned tuple as args for FormatOutput and saves formatting (tupleSize MUST == # of args)
    print(f"\n{formatSummary}")                             # Prints out summary w/ formatting --> Terminal
    SaveOutput(formatSummary, outPath)                      # Saves summary w/ formatting --> outPath/file.txt

if __name__ == "__main__":
    # Proper modulation of main.py - won't execute even when imported, unless script specifically called
    # __name__ attr. set to __main__ when executed but not imported, prevents accidental execution
    import csv, os
    main()