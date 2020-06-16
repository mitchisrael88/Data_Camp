# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xls = pd.ExcelFile('battledeath.xlsx')

# Print sheet names
print(xls.sheet_names)
