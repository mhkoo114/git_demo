from PyPDF2 import PdfReader

reader = PdfReader("C:\\Users\\USER\\Downloads\\Fake news detection based on machine learning.pdf")
for i, page in enumerate(reader.pages):
    print(f"Page {i+1} content length:", len(page.extract_text() or ""))
