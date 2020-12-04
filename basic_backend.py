from __future__ import annotations
from mvc_exceptions import *
from pathlib import Path
from re import findall
from os import remove, walk
from os.path import basename, join, exists
from PyPDF2 import PdfFileReader


class BackendClass:
    def __init__(self, observer):
        self.progressbar_max_value = 0
        self.progressbar_act_value = 0
        self.observer = observer

    def notify_max_val(self) -> None:
        """Trigger an update in subscriber."""
        self.observer.set_progress_bar_max_val(self)

    def notify_update(self) -> None:
        """Trigger an update in subscriber."""
        self.observer.update_progress_bar_value(self)

    def get_info_text(self):
        """Opens the info.txt and returns its content."""
        dir_ = "./info.txt"
        text = None
        if exists(dir_):
            with open(file=dir_, mode='r', encoding='utf-8') as f:
                text = f.read()
        return text

    def get_home_dir(self):
        """Return the home directory of the system."""
        return str(Path.home())

    def set_default_path(self, path):
        """Set default path for application."""
        dir_ = "./default.log"
        try:
            with open(dir_, 'w', encoding='utf-8') as f:
                f.write(path)
        except IOError as err:
            raise err

    def get_default_path(self):
        """Get default path."""
        dir_ = "./default.log"
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

    def walk_folder(self, folder_path):
        """Find and save all .pdf, .Pdf, .PDF files in given path."""
        pdf_files = []

        for root, dirs, files in walk(folder_path):
            for file in sorted(files):
                if file.endswith((".pdf", ".PDF", ".Pdf")):
                    pdf_files.append(join(root, file))

        if pdf_files:
            self.progressbar_max_value = len(pdf_files)
            self.notify_max_val()
            return pdf_files
        else:
            self.progressbar_max_value = 0
            raise NoPdfFilesFound('No .pdf, .Pdf or .PDF file(s) found!')

    def crawl_file(self, file, word):
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

    def crawl_files(self, path, word):
        """Crawl directory full of pdf files."""
        matches = []
        self.progressbar_act_value = 0
        self.notify_update()

        list_of_pdf = self.walk_folder(path)
        for pdf in list_of_pdf:
            # Update the bar
            self.progressbar_act_value += 1
            self.notify_update()
            matches.extend(self.crawl_file(pdf, word))
        return matches

    def save_results(self, path, results):
        """Save results to .txt file."""
        if path[0] and results:
            with open(file=path[0], mode="w", encoding='utf-8') as f:
                f.write(results)
        else:
            raise NoResults("No results to save!")

    def delete_log(self):
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
