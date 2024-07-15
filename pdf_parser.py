import PyPDF2
import os

def extract_info_from_pdf(pdf_folder):
    info = ""
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            with open(os.path.join(pdf_folder, pdf_file), 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                for page in range(reader.numPages):
                    info += reader.getPage(page).extract_text()
    return info
