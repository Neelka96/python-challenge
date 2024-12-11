# Python Challenge
`Module 3`  
`EdX(2U) & UT Data Analytics and Visualization Bootcamp`  
`Cohort UTA-VIRT-DATA-PT-11-2024-U-LOLC`    

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
This repository contains Python scripts for two data analysis challenges!  
Each script reads a CSV file, processes the data, formats it, and outputs  
a summary to the terminal and a text file saved to a designated path.  
### PyBank: 
Uses the CSV of monthly budget data from a bank to perform financial data  
analysis and provide a readable summary of the number of months, net profit,  
average of a change list, maximum(s), and minimums(s). [Link to PyBank main!](/PyBank/main.py)
### PyPoll: 
Uses the CSV of unique voter data from an election to perform election data  
analysis and provide a readable summary of the total voters, the number of  
votes for each candidate along with that percent of the total vote, and the  
winner(s) of the election based off popular vote. [Link to PyPoll main!](/PyPoll/main.py)
> [!WARNING]
> The CSV files in use were provided as learning material by EdX/UT  
> for use in their data viz course. Please be aware that data is most  
> likely auto-generated and not representative of any banks or elections.  

## Challenges Overview
Both challenges were originally completed using a global running of the script, but has  
since been modified for use as module/import, and to clarify algorithm process in main(). 

### PyBank
The PyBank script analyzes financial records to calculate:
- Total months in the dataset
- Net total profit/loss
- Average change in profit/loss between months
- Greatest increase and decrease in profits
     - Validates multiple max increase/decrease values

### PyPoll
The PyPoll script analyzes election data to determine:
- Total votes cast
- Votes and percentage of votes for each candidate
- Winner(s) based on popular vote
     - Validates multiple winners and outputs warning

## Setup and Usage
### Prerequisites
- Python 3.x
- Standard libraries: `csv` and `os` (included with Python)

### Limitations
- Doesn't verify unique voter ballot IDs
- Algorithms are basic/brute-force for the most part, so the complexity will raise linearly
- Readability: More Pythonic methods available in pandas (using basic methods per class instruction)

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
### StackOverflow Module Help
In the process of re-learning and practicing function calls and passing return values to the next  
function, I stumbled upon an interesting protocol that most .py files follow to prevent unintentional  
execution of imported files, and is a useful habit to have in terms of overall syntax.  
> @Mr Fooz. "What does if __name__ == "__main__": do?" Stack Overflow, January 7, 2009. https://stackoverflow.com/questions/419163/what-does-if-name-main-do  
### OpenAI ChatGPT
ChatGPT was utilized in this assignment for help generating the framework for this README.md.  
OpenAI's generativeAI was fed the rubric for this assignment to assist it in creating an accurate  
structure. README.md at this time differs largely in resemblence to original generated response.  
> OpenAI. (2024). ChatGPT (ChatGPT-4o) [Large language model]. https://chatgpt.com  

