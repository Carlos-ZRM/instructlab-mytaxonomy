from pdfminer.high_level import extract_text
from textblob import TextBlob

def extract_paragraphs_with_titles(pdf_path):
    # Extract text from the PDF
    text = extract_text(pdf_path)
    
    # Split the text into paragraphs
    paragraphs = text.split("\n\n")  # Assuming paragraphs are separated by double newlines
    
    # Process each paragraph to identify titles and content
    results = []
    for paragraph in paragraphs:
        blob = TextBlob(paragraph.strip())
        sentences = blob.sentences
        
        # Assume the first sentence is the title if it's short (e.g., less than 10 words)
        if sentences and len(sentences[0].words) < 10:
            title = str(sentences[0])
            content = " ".join(str(sentence) for sentence in sentences[1:])
        else:
            title = "Untitled"
            content = paragraph.strip()
        
        results.append({"title": title, "content": content})
    
    return results

# Example usage
pdf_path = "docs/Drug-Treatment-of-Cluster-Headache.pdf"  # Replace with your PDF file path
paragraphs_with_titles = extract_paragraphs_with_titles(pdf_path)

# Print the extracted paragraphs and their titles
for item in paragraphs_with_titles:
    print(f"Title: {item['title']}")
    print(f"Content: {item['content']}")
    print("-" * 50)