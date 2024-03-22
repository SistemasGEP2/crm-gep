from PyPDF2 import PdfWriter, PdfReader

pdf_writer = PdfWriter()
pdf_reader = PdfReader("Contrato_5A20293.pdf")

for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])


with open("Contrato_5A20293.pdf", "wb") as file:
    pdf_writer.write(file)
