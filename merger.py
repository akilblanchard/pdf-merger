import PyPDF2
import time
import sys

#Selects all PDFs to be merged
inputs = sys.argv[1:]

print("PDF Files to Merge:", inputs )

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        
        merger.append(pdf)

    print("Merging PDFs...")
    
    new_file = merger.write("merged.pdf")
    
    time.sleep(1.2)

    print("PDFs have been merged")

pdf_merger(inputs)





