import pdfplumber

with pdfplumber.open("Abir Ahsan_CV_webDev.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"
    
    with open("cv_content_v2.txt", "w", encoding="utf-8") as f:
        f.write(text)
