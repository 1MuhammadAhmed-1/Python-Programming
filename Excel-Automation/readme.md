# 🛠 Automation_Python

This folder contains a basic Python automation script that processes Excel data and generates a bar chart using the `openpyxl` library.

## 📁 Files

- `automation.py`: 
  - Reads an Excel file (`transactions.xlsx`)
  - Applies a 10% discount to each price in column C
  - Writes the corrected price to column D
  - Inserts a bar chart based on the corrected prices

- `transactions.xlsx`: 
  - Sample Excel file with price data in column C
  - Minimal dataset (only 2 rows) for testing and demonstration

## 🐍 How to Run

1. Make sure `openpyxl` is installed:
   ```bash
   pip install openpyxl
