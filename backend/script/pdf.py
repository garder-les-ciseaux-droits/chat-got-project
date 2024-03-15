import PyPDF2

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text
        
if __name__ == '__main__':
    extracted_text = extract_text_from_pdf('/Users/evanvosh/Documents/chat-gpt-project/backend/model/text.pdf')
    for text in extracted_text:
        print(text)
