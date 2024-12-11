# python-challenge

## Table of Contents
1. [Introduction](#introduction)
2. [Challenges Overview](#challenges-overview)
   - [PyBank](#pybank)
   - [PyPoll](#pypoll)
3. [Setup and Usage](#setup-and-usage)
4. [Expected Results](#expected-results)
5. [Files and Directory Structure](#files-and-directory-structure)
6. [Citations](#citations)

## Introduction
This repository contains Python scripts for two data analysis challenges: **PyBank** (financial data analysis) and **PyPoll** (election data analysis). Each script reads a CSV file, processes the data, and outputs a summary to the terminal and a text file.

## Challenges Overview

### PyBank
The **PyBank** script analyzes financial records to calculate:
- Total months in the dataset
- Net total profit/loss
- Average change in profit/loss between months
- Greatest increase and decrease in profits

### PyPoll
The **PyPoll** script analyzes election data to determine:
- Total votes cast
- Votes and percentage of votes for each candidate
- Winner(s) based on popular vote

## Setup and Usage
### Prerequisites
- Python 3.x
- Standard libraries: `csv` and `os` (included with Python)

### Instructions
1. Clone this repository.
2. Ensure the input CSV files are in the `Resources` folder.
3. Run the scripts from the command line:
   - PyBank: `python PyBank/main.py`
   - PyPoll: `python PyPoll/main.py`
4. Results will appear in the terminal and be saved to text files in the `analysis` folder.

## Expected Results
### PyBank Output
```
Financial Analysis
-------------------------
Total Months: 86
Total: $$22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

### PyPoll Output
```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## Files and Directory Structure
```
PyBank-and-PyPoll/
|— PyBank/
|   |— Resources/
|   |   — budget_data.csv
|   |— analysis/
|   |   — budget_analysis.txt
|   — main.py
|— PyPoll/
|   |— Resources/
|   |   — election_data.csv
|   |— analysis/
|   |   — election_analysis.txt
|   — main.py
```
This structure ensures all inputs and outputs are organized within their respective folders.

## Citations
# TODO-CITE OPENAI'S CHATGPT FOR ASSISTANCE IN GENERATING THE STRUCTURE OF THIS README.MD FILE GIVEN REQUIREMENTS OF EDX(2U) ASSIGNMENT MATERIALS AND MY VERY OWN SOURCE CODE

