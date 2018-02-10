from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


def add_to_pdf(test_list):
    iter = int(len(test_list) / 15) + 1

    for i in range(0,iter):
        index = i * 14
        pdf_creator(test_list[index:index+15],i)

def pdf_creator(test_list,formnum):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(15, 51)
    pdf.set_font('arial', 'B', 10.0)
    pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Yash Bharatula", border=0)


    # test_tuple_1 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_2 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_3 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
    # test_tuple_4 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_5 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
    # test_tuple_6 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_7 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
    # test_tuple_8 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_9 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_10 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
    # test_tuple_11 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_12 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
    # test_tuple_13 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451.666666", "$500", "M", "0", "$500")
    # test_tuple_14 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
    #
    # test_list = [test_tuple_1, test_tuple_2,test_tuple_3,test_tuple_4,test_tuple_5,test_tuple_6,test_tuple_7,test_tuple_8,test_tuple_9,test_tuple_10,test_tuple_11, test_tuple_12,test_tuple_13,test_tuple_14]
    ypos = 142
    xpos = 15
    for tuple in test_list:
        xpos = 13
        pdf.set_xy(xpos, ypos)
        pdf.set_font('arial', 'B', 8.0)

        pdf.cell(ln=0, h=5.0, align='L', w=3, txt=tuple[0][:25], border=0)
        xpos = xpos + 48
        pdf.set_xy(xpos, ypos)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[1][:10], border=0)
        xpos = xpos + 18
        pdf.set_xy(xpos, ypos)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[2][:10], border=0)
        xpos = xpos + 18
        pdf.set_xy(xpos, ypos)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[3][:10], border=0)
        xpos = xpos + 22
        pdf.set_xy(xpos, ypos)
        pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[4], border=0)
        ypos = ypos + 8.5
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

