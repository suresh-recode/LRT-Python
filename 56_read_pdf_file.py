import PyPDF2

# creating an object

reader = PyPDF2.PdfReader(r'C:\Users\Suresh Arunachalam\OneDrive - Intellius Recode Pvt.Ltd\Documents\Resume\Naukri_JagadeshKumar[4y_8m].pdf')

for page in reader.pages:
    print(page.extract_text())
    break