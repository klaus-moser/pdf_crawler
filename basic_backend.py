# basic_backend.py
from pathlib import Path

import mvc_exceptions as mvc_exc
from re import findall
from os import remove, walk
from os.path import basename, join, exists
from PyPDF2 import PdfFileReader

# global variable(s) where we keep the data
items = list()
pdfs = list()
default = str()


def get_info_text():
    """Opens the info.txt and returns its content."""
    dir_ = "./info.txt"
    text = None
    if exists(dir_):
        with open(file=dir_, mode='r', encoding='utf-8') as f:
            text = f.read()
    return text


def get_home_dir():
    """Return the home directory of the system."""
    return str(Path.home())


def set_default_path(path):
    """Set default path for application."""
    global default
    default = ""
    default = path


def get_default_path():
    """Set default path for application."""
    global default

    if default:
        return default
    else:
        raise mvc_exc.NoDefaultPathSet("No default path was set.")


def walk_folder(folder_path):
    """Find and save all .pdf, .Pdf, .PDF files in given path."""
    global pdfs
    global items
    items.clear()
    pdfs.clear()
    pdf_files = []

    for root, dirs, files in walk(folder_path):
        for file in sorted(files):
            if file.endswith((".pdf", ".PDF", ".Pdf")):
                pdf_files.append(join(root, file))

    if pdf_files:
        pdfs.extend(pdf_files)
    else:
        raise mvc_exc.MoPdfFilesFound('No .pdf, .Pdf or .PDF file(s) found!')


def crawl_pdf_file(file, word):
    """Search single file with the given word. Return list of Results or None."""
    global items

    matches = []

    # creating a pdf file object
    with open(file=file, mode='rb') as pdfFileObj:

        # creating a pdf reader object
        pdf_reader = PdfFileReader(pdfFileObj)

        for page in range(pdf_reader.numPages):
            # creating a page object
            page_obj = pdf_reader.getPage(page)

            # extracting text from page
            text = page_obj.extractText()

            # find all words
            words = findall(word, text)

            # If match, append to matches
            if words:
                matches.append((basename(file), page + 1, len(words)))
    return matches


def walk_pdf_files(word):
    """Walk through given Files and use crawl_pdf_files to extract information."""
    global items
    global pdfs

    results = list()

    for file in pdfs:
        results.extend(crawl_pdf_file(file=file, word=word))

    if results:
        items.extend(results)
    else:
        raise mvc_exc.NoResults('No Results!')


def delete_log():
    """Delete empty .log file (if existing)  to save memory."""
    del_ = False
    file = "crawler.log"

    if exists(file):
        with open(file=file, mode='r', encoding='utf-8') as f:
            if not f.readlines():
                del_ = True
        if del_:
            try:
                remove(file)
            except PermissionError:
                pass


if __name__ == '__main__':
    print(__file__)
