from pdfminer.high_level import extract_text
from textblob import TextBlob

def extract_titles_from_paragraphs(pdf_path):
    # Extract text from the PDF
    text = extract_text(pdf_path)
    
    # Split the text into paragraphs
    paragraphs = text.split("\n\n")  # Assuming paragraphs are separated by double newlines
    
    # Extract titles from each paragraph
    titles = []
    for paragraph in paragraphs:
        blob = TextBlob(paragraph.strip())
        sentences = blob.sentences
        
        # Assume the first sentence is the title if it's short (e.g., less than 10 words)
        if sentences and len(sentences[0].words) < 10:
            titles.append(str(sentences[0]))
    
    return titles

# Example usage
pdf_path = "docs/Drug-Treatment-of-Cluster-Headache.pdf"  # Replace with your PDF file path
titles = extract_titles_from_paragraphs(pdf_path)

# Print the extracted titles
for title in titles:
    print(f"Title: {title}")