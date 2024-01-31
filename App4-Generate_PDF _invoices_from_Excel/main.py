import pandas as pd
from fpdf import fpdf
# we need to create python list as there are multiple files.
# so we make use of glob module. point to the folder and the pattern of files to be read

pdf = FPDF(orientation="P", unit="mm", format="A4")
import glob

file_paths= glob.glob("invoices/*.xlsx")

for filepath in file_paths:
    df=pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)

