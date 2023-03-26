from pdfminer.high_level import extract_text

from .text_preprocessing import clean_text


def read_pdf(filepath: str) -> str:
    with open(filepath, "rb") as pdf_file:
        pdf_text = extract_text(pdf_file)
        return pdf_text


def parse_pdf(filepath: str) -> str:
    text = read_pdf(filepath)
    text = clean_text(text)
    return text
