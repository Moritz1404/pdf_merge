from sys import path
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import pathlib
import os
import subprocess
import platform

def merge_pdf(input_paths, output_path):
	writer = PdfFileWriter()
	for i in input_paths: 
		pdf_reader = PdfFileReader(i)
		for page in range(pdf_reader.getNumPages()):
			writer.addPage(pdf_reader.getPage(page))
	with open(output_path, "wb") as f_out:
		writer.write(f_out)


def check_file(input_paths):
	if os.path.isfile(str(input_paths[0])) and os.path.isfile(str(input_paths[1])):
		return True
	else:
		return False


def open_file(filepath):
	if platform.system() == 'Darwin':		#macOS
		subprocess.call(('open', filepath)) 
	elif platform.system() == 'Windows':	#Windows
		os.startfile(filepath)
	else:									#linux variants
		subprocess.call(('xdg-open', filepath))		
