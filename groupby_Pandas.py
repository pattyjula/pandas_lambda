# python3.6
# -*- coding: utf-8 -*-

"""Query big dataset, select columns to group by.
    Print output to a text file.
"""

# Import Dependencies
import sys
import pandas as pd

# Set variable
csv_path = "open_data_weekly_upload_occ_crm_data_i_u.csv"

# Read in CSV, specify columns
df = pd.read_csv(csv_path,usecols=['Area Name', 
    'Crime Code Description'])

# Apply lambda function to the value_counts       
summary_table=df.groupby('Area Name')['Crime Code Description']\
    .apply(lambda x: x.value_counts().head(3))
print(summary_table.head) 
with open('goats.txt','w') as f: print(summary_table.head, file=f)
                  

