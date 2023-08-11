from pathlib import Path
from PyPDF2 import PdfReader
from typing import Union
from typing import IO

def parse_pdfs(pdf_docs: Union[str, IO, Path]):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
