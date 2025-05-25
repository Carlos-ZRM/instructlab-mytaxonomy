from pdfminer.high_level import extract_text

def pdf_to_markdown(pdf_path, markdown_path):
    # Extract text from the PDF
    text = extract_text(pdf_path)
    
    # Convert the text to Markdown format (basic conversion)
    markdown_content = "# Extracted Content\n\n" + text.replace("\n", "  \n")  # Add Markdown line breaks
    
    # Write the Markdown content to a file
    with open(markdown_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

# Example usage
pdf_path = "docs/Drug-Treatment-of-Cluster-Headache.pdf"  # Replace with your PDF file path
markdown_path = "docs/Drug-Treatment-of-Cluster-Headache.md"  # Output Markdown file path
pdf_to_markdown(pdf_path, markdown_path)

print(f"Markdown file created at: {markdown_path}")