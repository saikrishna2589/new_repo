
import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF


#layout and font settings for one pdf document
pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_font(family="Times",size=16,style="B")

#filepaths stored for text files
filepaths=glob.glob("data/*.txt")

for filepath in filepaths:

    #steeming the path to extract just the filename i.e cats, dogs etc
    filename=Path(filepath).stem

    filename=filename.title()

    #adding one page per file
    pdf.add_page()
    pdf.set_font(family="Times",size=16,style="B")
    pdf.set_text_color(80,80,80)

    #giving the filename as text for each file i.e cat, dog etc
    pdf.cell(w=50,h=8,txt=filename,ln=1)


    #read the file contents
    'df=pd.read_csv(filepath,sep='###',header=None)
    with open(filepath,'r') as file:
        contents=file.readlines()


#using pdf.multi_cell method to read multiple lines in each file
    pdf.set_font(family="Times",size=8)
    pdf.set_text_color(80,80,80)
    for content in contents:
        pdf.multi_cell(w=0,h=8,txt=content)



    #only one output with multiple pages
pdf.output("Output/output.pdf")


