from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import pathlib
import os.path

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





















##if __name__=='__main__':
##	first_path = input("1.PDF path: ")
##	second_path = input("2.PDF path: ")
	
	#if os.path.isfile(first_path) and os.path.isfile(second_path):
	#	merge_pdf([first_path, second_path], "out.pdf")
	#	
	#	print("Merge successfully\n")
	#	print("Merged to " + str(pathlib.Path(__file__).parent.absolute()))

	#else:
	#	print("Path not existing!")
	#	exit(1)

##	if check_file([first_path, second_path]) is True:
##		print('geil')
#	else:
#		exit(1)