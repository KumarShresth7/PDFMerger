import PyPDF2
import os

def merge_pdfs(input_paths, output_path):
    """Merge multiple PDF files into a single PDF."""
    pdf_writer = PyPDF2.PdfWriter()
    
    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

if __name__ == "__main__":
    # Example usage
    input_files = ["D:\\Coding\\Python\\PDFMerger\\Rashmeet_Singh_102203851_assignment2.pdf", "D:\\Coding\\Python\\PDFMerger\\YashKukshal_ass3.pdf"]  # List of PDF files to merge
    output_file = "merged_output.pdf"  # Output file name

    # Merge PDFs
    merge_pdfs(input_files, output_file)
    print("PDFs merged successfully.")
