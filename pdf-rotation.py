"""
Script that takes in cmd lines and rotates pdf file 
in given angle.
"""

import argparse
from PyPDF4 import PdfFileReader as PdfReader
from PyPDF4 import PdfFileWriter as PdfWriter
import os

def rotate_and_save(input_pdf, output_pdf, rotation_angle):
    """
    Rotates and saves new PDF.
    """
    if not os.path.exists(input_pdf):
        print(f"Error: {input_pdf} does not exist.")
        return

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page._rotate(rotation_angle)
        writer.addPage(page)

    with open(output_pdf, "wb") as out_file:
        writer.write(out_file)
    print(f"PDF saved as {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Rotate PDF pages and save the result.")
    parser.add_argument("input_pdf", help="The input PDF file to rotate.")
    parser.add_argument("output_pdf", help="The output PDF file to save the rotated PDF.")
    parser.add_argument("rotation_angle", type=int, help="The rotation angle (in degrees).")

    args = parser.parse_args()
    rotate_and_save(args.input_pdf, args.output_pdf, args.rotation_angle)

if __name__ == "__main__":
    main()
