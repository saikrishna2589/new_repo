# third party library fpdf (to be installed)

# this creates pdf object instance
from fpdf import FPDF

import pandas as pd

# orientation="p" is portrait. you can goto the implemetation to check documentation.
# 'mm' unit is not for font but for other purpose
pdf = FPDF(orientation="P", unit="mm", format="A4")

# the below command makes sure pages are not broken automatically as we need to set pages for footers.
pdf.set_auto_page_break(auto=False, margin=0)

# type of pdf is a python object. we need to convert it to an actual document.
print(type(pdf))

# reading the file that contains csv data
df = pd.read_csv("topics.csv")

# looping over dataset
for index, row in df.iterrows():
    pdf.add_page()

    #set the header
    pdf.set_font(family="Times", style="B", size=24)

    # setting font to gray
    pdf.set_text_color(100, 100, 100)

    # width =0 will stretch the cell to complete page. height =12 is hieght of cell
    pdf.cell(w=0, h=12, txt=row["Topic"])

    # adding a line below .x1,y1 coordinates will be starting point and x2,y2 ending point
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    # set the footer
    # here we are adding break line at 278mm height (A4 size total height is 298).we do this to add footer
    pdf.ln(273)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # we need to add 2 pages for 1st row i.e of topic variables, 3 pages for list and so on how to achieve that? we
    # can use range method. range(3) gives us range(0,3) as output.#converting to list(range(3) will give output as
    # [0,1,2]. so range is kind of a list object

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer for additional pages
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
