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

# Import Libraries
import csv
import os


def AnalyzeBudgetCSV(inStream):
    totalMonths = 0
    netProfit = 0
    # Change & date list are connected via index
    changeList = [] # changeList will collect differentials between neighboring values
    dateList = []   # dateList will store the date the changeValue is subtracted from
    maxVal = ['', 0]
    minVal = ['', 0]

    # Open csv path var and begin reading
    # csv path set to var > open csv file under new alias > start reading under alias
    # path > open(path) = path.open() > readerVar = csv.Reader(path.open())
    with open(inStream, 'r') as inData:
        csvReader = csv.reader(inData, delimiter = ",")     # Create reading object for csv
        header = next(csvReader)    # Skip header row
        priorRow = next(csvReader)  # Save and skip 1st csv row for changeList[]
        priorRow[1] = int(priorRow[1])  # Recast for permanent int usage

        netProfit += priorRow[1]    # Add current value into summed profit/losses
        totalMonths += 1    # Count first row not included in "for" loop
        
        for row in csvReader:
            row[1] = int(row[1])   # Recasting for permanent int usage
            netProfit += row[1]    # Calculate net profit/loss
            totalMonths += 1    # Find total months listed in csv
            
            budgetChg = row[1] - priorRow[1] # Calc Current Change
            changeList.append(budgetChg) # Appends differential to list
            dateList.append(row[0]) # Appends current date to change list

            if maxVal[1] < budgetChg:       # Checks if current chg > than max chg
                maxVal[0] = row[0]      # If so -> Set maxVal list to budget chg & date
                maxVal[1] = budgetChg
                if len(maxVal) > 2:     # If replacing maxVal delete other values
                    del maxVal[2:]
            elif maxVal[1] == budgetChg:    # Checks if current chg = max chg
                maxVal.append(row[0])   # If so -> Add to list (can be deleted later)
                maxVal.append(budgetChg)
            
            if minVal[1] > budgetChg:    # Checks if current chg < then min chg
                minVal[0] = row[0]      # If so -> Set minVal list to budget chg & date
                minVal[1] = budgetChg
                if len(minVal) > 2:     # If replacing minVal delete other values
                    del minVal[2:]
            elif minVal[1] == budgetChg:    # Checks if current chg = max chg  
                minVal.append(row[0])   # If so -> Add to list (can be deleted later)
                minVal.append(budgetChg)            
            priorRow = row  # Sets current row as "prior" for next iteration
        
        avgChg = format(sum(changeList)/len(changeList), ".2f")
        # zipChanges = zip(dateList, changeList) --> Creates 1 zip object to hold both dates and changes (not exported)
    return totalMonths, netProfit, avgChg, maxVal, minVal

def FormatOutput(months, profits, average, maximum, minimum):
    # Printing statements w/ desired terminal output formatting
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

def SaveOutput(outStream, saveContent):
    # Output method - writing formatted analysis to .txt file
    # Does it need to be in csv formatting or in the same format as analysis?
    with open(outStream, 'w') as outData:
        outData.write(saveContent)
    return None     # Personal preference to return void/null for no actual return value



# This is where the code executes and calls functions
if __name__ == "__main__":      # __name__ is always set to __main__ when executed. 
    inPath = os.path.join("Resources", "budget_data.csv")
    outPath = os.path.join("analysis", "budget_analysis.txt")
    
    budgetSummary = AnalyzeBudgetCSV(inPath)
    formatSummary = FormatOutput(*budgetSummary)    # * Unpacks returned tupple into arguments for FormatOutput
    
    print(f"\n{formatSummary}")

    SaveOutput(outPath, formatSummary)