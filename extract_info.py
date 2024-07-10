import tabula
import fitz     # This is the library associated with PyMuPDF
import pdfplumber
from pdfminer.high_level import extract_text


# Text extraction using fitz
def text_extraction_fitz(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Link extraction using fitz
def link_extraction_fitz(pdf_path):
    doc = fitz.open(pdf_path)
    links=[]
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        links.append(page.get_links())
    return links

# Image extraction using fitz
def image_extraction_fitz(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for image in page.get_images(full=True):
            xref = image[0]
            base_image = doc.extract_image(xref=xref)
            images.append(base_image)
    return images

# Text extraction using pdf plumber 
def text_extraction_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# PDF plumber can be used to extract the table content precisely.
# It will print row wise content of the table.
def table_extraction_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            print(page.extract_tables())


# Extracting content of table using tabula
def table_extraction_tabula(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    return tables



# Defining main method
def main():
    pdf_path = "./complex_input_files/sample.pdf"
    text = text_extraction_fitz(pdf_path=pdf_path)
    print("Text extracted using PyMuPDF \n")
    print(text)
    print("\n")

    links = link_extraction_fitz(pdf_path=pdf_path)
    print("Links extracted using the PyMuPDF \n")
    print(links)
    print("\n")

    images = image_extraction_fitz(pdf_path=pdf_path)
    print("Image extrcted using PyMuPDF")
    #print(images) # It will pixel values, for viwing image need to plot 
    print("\n")

    texts = text_extraction_pdfplumber(pdf_path=pdf_path)
    print("Text extraction using PDF Plumber")
    print(text)
    print("\n")

    table_extraction_pdfplumber(pdf_path=pdf_path)
    print("\n")

    tables = table_extraction_tabula(pdf_path)
    print("\nTables extracted using tabula")
    for i, table in enumerate(tables):
        print(f"Table {i+1}:")
        print(table)
    

if __name__ == "__main__":
    main()