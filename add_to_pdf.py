import io
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

pdf = FPDF()
pdf.add_page()
pdf.set_xy(15, 51)
pdf.set_font('arial', 'B', 10.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Yash Bharatula", border=0)

test_tuple_1 = ("100 BitcoindFDfdfdfdfdfdfdfdasdfghjklqwertyuiop", "02/03/2018", "02/10/2018", "$451", "$500", "M", "0", "$500")
test_tuple_2 = ("hi", "02/3/2018", "02/10/2018", "$800", "$1000", "M", "0", "$500")
test_list = [test_tuple_1, test_tuple_2]
ypos = 143
xpos = 15
for tuple in test_list:
    xpos = 13
    pdf.set_xy(xpos, ypos)
    pdf.set_font('arial', 'B', 10.0)

    pdf.cell(ln=0, h=5.0, align='L', w=3, txt=tuple[0][:25], border=0)
    xpos = xpos + 47
    pdf.set_xy(xpos, ypos)
    pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[1][:10], border=0)
    xpos = xpos + 17
    pdf.set_xy(xpos, ypos)
    pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[2], border=0)
    # xpos = xpos + 5
    # pdf.set_xy(xpos, ypos)
    # pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[3], border=0)
    # xpos = xpos + 5
    # pdf.set_xy(xpos, ypos)
    # pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[4], border=0)
    # xpos = xpos + 5
    # pdf.set_xy(xpos, ypos)
    # pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[5], border=0)
    # xpos = xpos + 5
    # pdf.set_xy(xpos, ypos)
    # pdf.cell(ln=0, h=5.0, align='L', w=0, txt=tuple[6], border=0)
    ypos = ypos + 8

pdf.output('test.pdf', 'F')

existing_pdf = PdfFileReader(open("f8949_tax_form.pdf", "rb"))
edited_pdf = PdfFileReader(open('test.pdf','rb'))
output = PdfFileWriter()
page = edited_pdf.getPage(0)
page.mergePage(existing_pdf.getPage(0))
output.addPage(page)
output_file = open("merged.pdf", "wb")
output.write(output_file)
output_file.close()
