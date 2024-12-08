# Neel Agarwal @Neelka96
# Last Updated: 12.7.2024

# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the 
# financial records of your company.**

# You will be given a financial dataset called **budget_data.csv**. The dataset is # composed of two columns: **"Date" and "Profit/Losses"**.
# Your task is to create a Python script that analyzes the records to calculate 
# each of the following values:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of 
# those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and # export a text file with the results.


# Desired output:

# Financial Analysis
# --------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# -----------------------------------------------------
# Test data for repeating max's and min's
# Mar-17,878810
# Apr-17,-946748
# May-17,-910775
# Jun-17,951227

# Import Libraries
import csv
import os


def AnalyzeBudgetCSV(inStream):
    totalMonths = 0
    netProfit = 0
    # Change & date list are connected via index
    changeList = [] # changeList will collect differentials between neighboring values
    dateList = []   # dateList will store the date the changeValue is subtracted from

    # Open csv path var and begin reading
    # csv path set to var > open csv file under new alias > start reading under alias
    # path > open(path) = path.open() > readerVar = csv.Reader(path.open())
    with open(inStream, 'r') as inFile:
        csvReader = csv.reader(inFile, delimiter = ",")     # Create reading object for csv
        header = next(csvReader)    # Skip header row
        priorRow = next(csvReader)  # Save and skip 1st csv row for changeList[]
        priorRow[1] = int(priorRow[1])  # Recast for permanent int usage

        netProfit += priorRow[1]    # Add current value into summed profit/losses
        totalMonths += 1    # Count first row not included in "for" loop
        
        # Creating the List of budget changes (very important list)
        for row in csvReader:
            row[1] = int(row[1])   # Recasting for permanent int usage
            netProfit += row[1]    # Calculate net profit/loss
            totalMonths += 1    # Find total months listed in csv

            budgetChg = row[1] - priorRow[1] # Calc Current Change
            priorRow = row  # Reset priorRow to the current row iteration for next loop
            dateList.append(row[0]) # Appends current date to change list
            changeList.append(budgetChg) # Appends differential to list

        avgChg = format(sum(changeList)/len(changeList), ".2f")
        # Calls functions defined in this .py file made to ensure there are not multiple extremeties
        maxVal = MultipleExtremes(dateList, changeList, "max")    # Checks if there are multiple greatest increases
        minVal = MultipleExtremes(dateList, changeList, "min")    # Checks if there are multiple greatest decreases
    return totalMonths, netProfit, avgChg, maxVal, minVal

# Function to format output for both terminal and for saving to a file
# Method is to continuously concatanate str var that will be returned
def FormatOutput(months, profits, average, maximum, minimum):
    outString = "Financial Analysis\n"
    outString += f"{'-' * 25}\n"
    outString += f"Total Months: {months}\n"
    outString += f"Total: ${profits}\n"
    outString += f"Average Change: ${average}\n"
    if len(maximum) == 2:
        outString += f"Greatest Increase in Profits: {maximum[0]} (${maximum[1]})\n"
    else:   # Accounting for maxVal list greater than length 2
        for n in range(int(len(maximum) / 2)):
            outString += f"Greatest Increase in Profits: {maximum[n*2]} (${maximum[(n*2)+1]})\n"
    if len(minimum) == 2:
        outString += f"Greatest Decrease in Profits: {minimum[0]} (${minimum[1]})\n"
    else:   # Accounting for minVal list greater than length 2
        for n in range(int(len(minimum) / 2)):
            outString += f"Greatest Decrease in Profits: {minimum[n*2]} (${minimum[(n*2)+1]})\n"
    
    return outString

# Function to export/save formatted output to a .txt file, path > PyBank/analysis/budget_analysis.txt
def SaveOutput(saveContent, outStream):
    with open(outStream, 'w') as outData:
        outData.write(saveContent)
    return None     # Personal preference to return void/null for no actual return value

# Args: <list of strings>, <list of integers>, <string>
def MultipleExtremes(dates, values, max_or_min):
    trueExtreme = None  # Not needed init of trueExtreme (if...else block doesn't prevent global inits)
    if max_or_min == "max":     # Finding max or min (function will be called once for each)
        trueExtreme = max(values)
    elif max_or_min == "min":
        trueExtreme = min(values)
    else:
        quit(f"Source code: <max_or_min> arg '{max_or_min}' not valid")
    # Building list of other potential indeces where extremes were found
    # Using enumerate() to create list of indeces alongside each value - links to dates
    otherExtremes = [index for index, extreme in enumerate(values) if extreme == trueExtreme]
    # Create list built for output in the format the other modules are expecting
    # [date, value] or if multiple values [date, value, date, value, etc...]
    outputExtremes = []
    for index in otherExtremes:
        outputExtremes.append(dates[index])
        outputExtremes.append(trueExtreme)
    return outputExtremes

def main():
    inPath = os.path.join("Resources", "budget_data.csv")
    outPath = os.path.join("analysis", "budget_analysis.txt")
    
    # Calling built functions in module form allows for psuedocode-esque reading of purpose
    budgetSummary = AnalyzeBudgetCSV(inPath)
    formatSummary = FormatOutput(*budgetSummary)    # * Unpacks returned tupple into arguments for FormatOutput
    print(f"\n{formatSummary}")
    SaveOutput(formatSummary, outPath)

# This is where the code executes and calls functions
# Callback to c++ :)
if __name__ == "__main__":      # __name__ is always set to __main__ when executed. 
    main()