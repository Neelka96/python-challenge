# Neel Agarwal @Neelka96
# Last Updated: 12.4.2024

# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
# 
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#
# Desired output:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# Import Libraries
import csv
import os

# Set .csv and .txt paths for importing and exporting
importPath = os.path.join("Resources", "budget_data.csv")
exportPath = os.path.join("analysis", "budget_analysis.txt")

# Global variables initializations
totalMonths = 0
netProfit = 0
changeList = [] # changeList will collect differentials between neighboring values
maxVal = []
minVal = []
avgChange = 0

# Open csv path var and begin reading
# csv path set to var > open csv file under new alias > start reading under alias
# path > open(path) = path.open() > readerVar = csv.Reader(path.open())
with open(importPath, 'r') as importData:
    csvReader = csv.reader(importData, delimiter = ",")
    header = next(csvReader)    # Skip header row
    
    priorRow = next(csvReader)  # Save and skip 1st csv row for changeList[]
    totalMonths += 1    # Count first row not included in "for" loop
    
    maxVal = priorRow   # Set max/min values arrays to 1st entry
    minVal = priorRow

    for row in csvReader:
        totalMonths += 1    # Find total months listed in csv
        netProfit += int(row[1])    # Calculate net profit/loss
        
        if (maxVal[1] < row[1]):
            maxVal = row
        elif (minVal[1] > row[1]):
            minVal = row

        budgetChange = int(row[1]) - int(priorRow[1]) # Calculate current change
        changeList.append(budgetChange) # Appends differential to list
        priorRow = row  # Sets current row as "prior" for next iteration

    avgChange = sum(changeList) # Using a "for" loop is OK here too
    avgChange /= (totalMonths - 1)  # avgChange /= len(changeList) is OK too

print(f"Months: {totalMonths}, Profit/Loss: {netProfit}, Avg Change: {avgChange}")
print(f"Greatest Increase in Profits: {minVal[0]} ({maxVal[1]})") 
print(f"Greatest Decrease in Profits: {minVal[0]} ({minVal[1]})")