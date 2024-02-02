import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path
# we need to create python list as there are multiple files.
# so we make use of glob module. point to the folder and the pattern of files to be read


file_paths= glob.glob("invoices/*.xlsx")

for filepath in file_paths:

    #read excel file
    df=pd.read_excel(filepath,sheet_name="Sheet 1")

    #create pdf object
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    #add pdf page
    pdf.add_page()

    #the Path().stem extracts the filename from filepath. for ex-10001-2023.1..18.xlsx.stem gives 10001-2023.1.18 without the extension
    filename= Path(filepath).stem


    # we then split the filename at "-" and extract the first item of the list,which is the invoice number
    invoice_nr,date=filename.split("-")
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}",ln=1)


    date= filename.split("-")[1]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date.{date}")


    pdf.output(f"PDF_output/{filename}.pdf" )






