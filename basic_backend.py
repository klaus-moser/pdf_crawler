import mvc_exceptions as mvc_exc
from pathlib import Path
from re import findall
from os import remove, walk
from os.path import basename, join, exists
from PyPDF2 import PdfFileReader

# global variable(s) where we keep the data
pdfs = list()


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
    dir_ = "./default.txt"
    try:
        with open(dir_, 'w', encoding='utf-8') as f:
            f.write(path)
    except IOError as err:
        raise err


def get_default_path():
    """Get default path."""
    dir_ = "./default.txt"
    path_ = ""
    if exists(dir_):
        try:
            with open(dir_, 'r', encoding='utf-8') as f:
                path_ = f.read()
            return path_
        except FileNotFoundError as err:
            raise err
    else:
        return path_


def walk_folder(folder_path):
    """Find and save all .pdf, .Pdf, .PDF files in given path."""
    global pdfs
    pdfs.clear()
    pdf_files = []

    for root, dirs, files in walk(folder_path):
        for file in sorted(files):
            if file.endswith((".pdf", ".PDF", ".Pdf")):
                pdf_files.append(join(root, file))

    if pdf_files:
        pdfs.extend(pdf_files)
        return pdf_files
    else:
        raise mvc_exc.NoPdfFilesFound('No .pdf, .Pdf or .PDF file(s) found!')


def crawl_file(file, word):
    """Search single file with the given word. Return list of Results or None."""
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


def crawl_files(path, word):
    """Crawl directory full of pdf files."""
    matches = []

    list_of_pdf = walk_folder(path)
    for pdf in list_of_pdf:
        matches.append(crawl_file(pdf, word))
    return matches


def save_results(path, results):
    """Save results to .txt file."""
    if results:
        pass
        # Write file

    else:
        raise mvc_exc.NoResults("No results to save!")


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
