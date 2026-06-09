import os
import sys
from PyPDF2 import PdfMerger


def merge_pdfs(pdf_files: list[str], output_path: str) -> None:
    """Merge a list of PDF files into a single output PDF."""
    if not pdf_files:
        print("Error: No PDF files provided.")
        sys.exit(1)

    merger = PdfMerger()

    for pdf in pdf_files:
        if not os.path.isfile(pdf):
            print(f"Error: File not found - {pdf}")
            sys.exit(1)
        if not pdf.lower().endswith(".pdf"):
            print(f"Error: Not a PDF file - {pdf}")
            sys.exit(1)
        print(f"  Adding: {pdf}")
        merger.append(pdf)

    merger.write(output_path)
    merger.close()
    print(f"\nMerged PDF saved to: {output_path}")


def main():
    # ---------------------------------------------------------------
    # Option 1: Hard-code your PDF paths here for quick use
    # ---------------------------------------------------------------
    pdf_list = [
        r"C:\Users\file1.pdf",
        r"C:\Users\file2.pdf"
                ]
    output_file = r"C:\Users\merged_output.pdf"
    merge_pdfs(pdf_list, output_file)
    return

    # ---------------------------------------------------------------
    # Option 2: Pass PDF paths as command-line arguments
    #   Usage: python merge_pdf.py file1.pdf file2.pdf ... output.pdf
    # ---------------------------------------------------------------
    if len(sys.argv) < 3:
        print("Usage: python merge_pdf.py <input1.pdf> <input2.pdf> ... <output.pdf>")
        print("\nExample:")
        print("  python merge_pdf.py doc1.pdf doc2.pdf doc3.pdf merged.pdf")
        sys.exit(1)

    *input_pdfs, output_pdf = sys.argv[1:]
    print(f"\nMerging {len(input_pdfs)} PDF(s)...")
    merge_pdfs(input_pdfs, output_pdf)


if __name__ == "__main__":
    main()
