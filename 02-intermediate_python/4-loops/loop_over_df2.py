# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab[0:3]) + ": " + str(row['cars_per_cap']))
    
