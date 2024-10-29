# PDFScripts
Scripts to run PDF actions using PyPDF4.

PDF Rotator
A simple command-line tool to rotate PDF pages and save the result using Python and PyPDF4.

Features
Rotate PDF pages by a specified angle

Save the rotated PDF to a new file

Command-line interface for easy usage

Requirements
Python 3.x

PyPDF4

Installation
Clone the repository:

sh

Copy
git clone https://github.com/yourusername/pdf-rotator.git
cd pdf-rotator
Install the required packages:

sh

Copy
pip install PyPDF4
Usage
Run the script from the command line with the following syntax:

sh

Copy
python rotate_pdf.py <input_pdf> <output_pdf> <rotation_angle>
<input_pdf>: Path to the input PDF file

<output_pdf>: Path to save the rotated PDF file

<rotation_angle>: The rotation angle in degrees (e.g., 90, 180, 270)

Example
sh

Copy
python rotate_pdf.py input.pdf rotated_output.pdf 90
This example rotates the pages in input.pdf by 90 degrees and saves the result to rotated_output.pdf.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Fork the repository.

Create your feature branch: git checkout -b feature/AmazingFeature

Commit your changes: git commit -m 'Add some AmazingFeature'

Push to the branch: git push origin feature/AmazingFeature

Open a pull request.
