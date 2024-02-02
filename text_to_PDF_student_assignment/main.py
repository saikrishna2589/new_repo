
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

    #giving the text as filename for each file i.e cat, dog etc
    pdf.cell(w=50,h=8,txt=filename)
    print(filename)

    #only one output with multiple pages
pdf.output("Output/output.pdf")


