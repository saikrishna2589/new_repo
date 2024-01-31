import pandas as pd

# we need to create python list as there are multiple files.
# so we make use of glob module. point to the folder and the pattern of files to be read

import glob

file_paths= glob.glob("invoices/*.xlsx")

for filepath in file_paths:
    df=pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)