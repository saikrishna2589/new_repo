import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path
# we need to create python list as there are multiple files.
# so we make use of glob module. point to the folder and the pattern of files to be read


file_paths= glob.glob("invoices/*.xlsx")

for filepath in file_paths:

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


  #adding the date
    date = filename.split("-")[1]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date.{date}",ln=1)

    # read excel file
    # for each row in the file,write the text of the relevant row[column].no ln=1 in the beginning as we want side -side
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # here we are extrating the column names and then adding each column name to one row with a border
    # we also remove underscores

    # we are getting the column names and replacing the '_' with space
    columns_name = list(df.columns)
    columns_name = [item.replace("_", " ").title() for item in columns_name]

    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns_name[0], border=1)
    pdf.cell(w=70, h=8, txt=columns_name[1], border=1)
    pdf.cell(w=30, h=8, txt=columns_name[2], border=1)
    pdf.cell(w=30, h=8, txt=columns_name[3], border=1)
    pdf.cell(w=30, h=8, txt=columns_name[4], border=1, ln=1)

    # looping through each row
    for index,row in df.iterrows():
        pdf.set_font(family="Times",size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]),border=1)
        pdf.cell(w=70,h=8,txt=str(row["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1,ln=1)


# adding the total sum row

    total_sum=df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30,h=8,txt=f"The total price is {total_sum}",ln=1)


    pdf.set_font(family="Times", size=10)
    pdf.cell(w=25, h=8, txt=f"PythonHow")
    pdf.image("pythonhow.png",w=10)

    pdf.output(f"PDF_output/{filename}.pdf")












