import fitz  # PyMuPDF
from textblob import TextBlob

def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                text = ""
                for line in block["lines"]:
                    for span in line["spans"]:
                        text += span["text"] + " "
                
                text = text.strip()

                if not text:
                    continue

                # Heuristic: Titles are often short and bold or large
                if len(text.split()) <= 10 and text.isupper() or text.istitle():
                    section_type = "Title"
                else:
                    section_type = "Paragraph"

                sections.append({"type": section_type, "text": text})
    
    return sections

def extract_noun_phrases(text):
    blob = TextBlob(text)
    return blob.noun_phrases

# Example usage
pdf_file = "docs/Drug-Treatment-of-Cluster-Headache.pdf"  # Replace with your PDF file path
sections = extract_pdf_content(pdf_file)

for section in sections:
    print(f"Type: {section['type']}")
    print(f"Text: {section['text']}")
    if section['type'] == "Paragraph":
        context = extract_noun_phrases(section["text"])
        print(f"Noun Phrases: {context}")
    print("---")