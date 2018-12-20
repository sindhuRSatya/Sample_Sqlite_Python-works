


import sys



from pandas import DataFrame,read_csv

import pandas as pd




read_employees = pd.read_csv(r'emp_pro.csv')

df = DataFrame(read_employees)

print (df) 