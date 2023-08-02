# -*- coding: utf-8 -*-

import subprocess
import pandas as pd

# List of your scripts
scripts = ["civilbottrue.py"]#add more by inserting comma adn writing the scriptname.py file in bracket

# Run your scripts
for script in scripts:
    subprocess.call(["python", script])

# List of your Excel files
files = ["filtered_table_data1.xlsx"] #same concept as ln7 comment

# Read them in
excels = [pd.ExcelFile(name) for name in files]

# Turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# Delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# Concatenate them
combined = pd.concat(frames)

# Write it out
combined.to_excel("combined.xlsx", header=False, index=False)
