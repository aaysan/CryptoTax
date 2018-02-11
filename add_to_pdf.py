from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from transactions import Transaction

# a =  Transaction("test1","BTC","0.000009","02/02/2018","01/01/2018","456.8", "USD")
# b = []
# b.append(a)

def add_to_pdf(test_list):
    iter = int(len(test_list) / 15) + 1

    for i in range(0,iter):
        idx = i * 14
        pdf_creator(test_list[idx:idx+14],i)

def pdf_creator(test_list,formnum):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(15, 51)
    pdf.set_font('arial', 'B', 10.0)
    pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Rahul 'trashed' Patni", border=0)
    pdf.set_x(130)
    pdf.cell(ln=0, h=5,align='L',w=0,txt="123-45-6789", border=0)
    soldsum = 0
    boughtsum = 0
    ypos = 142
    for tuple in test_list:
        xpos = 13
        pdf.set_xy(xpos, ypos)
        pdf.set_font('arial', 'B', 7.5)
        description = tuple.description + " (" + tuple.crypto_currency + " " + tuple.crypto_amount + ")"
        pdf.cell(ln=0, h=5.0, align='L', w=3, txt=description[:35], border=0)
        xpos = xpos + 48
        pdf.set_xy(xpos, ypos)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple.date_acquired[:10], border=0)
        xpos = xpos + 18
        pdf.set_xy(xpos, ypos)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple.date_sold[:10], border=0)
        xpos = xpos + 18
        pdf.set_xy(xpos, ypos)


        proceeds = tuple.currency + " " + tuple.proceeds

        if tuple.date_sold != "-":
            proceeds = proceeds.replace("-","")
            pdf.cell(ln=0, h=5.0, align='L', w=0, txt=proceeds[:10], border=0)
            soldsum = soldsum + float(tuple.proceeds)
        else:
            pdf.cell(ln=0, h=5.0, align='L', w=0, txt="-", border=0)

        xpos = xpos + 22
        pdf.set_xy(xpos, ypos)

        if tuple.date_acquired != "-":
            pdf.cell(ln=0, h=5.0, align='L', w=0, txt=proceeds[:10], border=0)
            boughtsum = boughtsum + float(tuple.proceeds)
        else:
            pdf.cell(ln=0, h=5.0, align='L', w=0, txt="-", border=0)

        ypos = ypos + 8.5

    ypos = 264
    xpos = 97
    pdf.set_xy(xpos, ypos)
    pdf.cell(ln=0, h = 5.0, align='L',w=0, txt=str(-1*soldsum),border=0)
    xpos = 119
    pdf.set_xy(xpos, ypos)
    pdf.cell(ln=0, h=5.0, align='L',w=0, txt=str(boughtsum), border=0)

    pdf.add_page()
    pdf.output('test.pdf', 'F')

    existing_pdf = PdfFileReader(open("f8949_tax_form.pdf", "rb"))
    edited_pdf = PdfFileReader(open('test.pdf','rb'))
    output = PdfFileWriter()
    page = edited_pdf.getPage(0)
    page.mergePage(existing_pdf.getPage(0))
    output.addPage(page)
    page2 = edited_pdf.getPage(1)
    page2.mergePage(existing_pdf.getPage(1))
    output.addPage(page2)
    path = "tax_form"+str(formnum)+".pdf"
    output_file = open(path, "wb")
    output.write(output_file)
    output_file.close()
    os.remove("test.pdf")
#
# add_to_pdf(b)
