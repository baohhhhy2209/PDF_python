import PyPDF2 
def read_metadata(pdf_file): 
	pdf_reader = PyPDF2.PdfReader(pdf_file)

	metadata = pdf_reader.metadata 


	print("Metadata of the PDF file is: ")
	for key,value in metadata.items():
		print(f"{key}: {value}")

read_metadata('merged.pdf')

def add_metadata(inpput_file, output_file, author): 
	pdf_reader = PyPDF2.PdfReader(inpput_file)
	pdf_writer = PyPDF2.PdfWriter()

	for page_num in range(len(pdf_reader.pages)): 
		pdf_writer.add_page(pdf_reader.pages[page_num])

	metadata = {
		'/Title': title, 
		'/Author': author 
	}

	pdf_writer.add_metadata(metadata)

	with open(output_file, 'wb') as out: 
		pdf_writer.write(out)

	print(f"PDF file with updated metadata is saved as {output_file}")

add_metadata('merged.pdf', 'metadata_added.pdf', 'Sample File for Python Code', 'Dr. Bao Huy')