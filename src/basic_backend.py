#!/usr/bin/env python3

# Filename: basic_backend.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" Basic/Static Backend."""

from __future__ import annotations
from os.path import basename, join, exists
from PyPDF2 import PdfFileReader
from pathlib import Path
from re import findall
from os import walk

from mvc_exceptions import *


class BackendClass:

    def __init__(self, observer):
        self.progressbar_max_value = 0
        self.progressbar_act_value = 0
        self.observer = observer

    def notify_max_val(self) -> None:
        """
        Trigger an update in subscriber.
        :return:
        """
        self.observer.set_progress_bar_max_val(self)

    def notify_update(self) -> None:
        """
        Trigger an update in subscriber.
        :return:
        """
        self.observer.update_progress_bar_value(self)

    @staticmethod
    def get_info_text() -> None:
        """
        Opens the info.txt and returns its content.
        :return:
        """
        dir_ = "./resources/files/info.txt"
        text = None

        if exists(dir_):
            with open(file=dir_, mode='r', encoding='utf-8') as f:
                text = f.read()
        return text

    @staticmethod
    def get_home_dir() -> str:
        """
        Return the home directory of the system.
        :return: String of home dir.
        """
        return str(Path.home())

    @staticmethod
    def set_default_path(path: str) -> None:
        """
        Set default path for application.
        :param path: String of new default path.
        :return:
        """
        dir_ = "./default.log"

        try:
            with open(dir_, 'w', encoding='utf-8') as f:
                f.write(path)
        except IOError as err:
            raise err

    @staticmethod
    def get_default_path() -> str:
        """
        Get default path.
        :return: String of default path.
        """
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

    def walk_folder(self, folder_path: str) -> list:
        """
        Find and save all .pdf, .Pdf, .PDF files in given path.
        :param folder_path: Path of folder.
        :return: List of all .pdf files.
        """
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

    @staticmethod
    def crawl_file(file: str, word: str) -> list:
        """
        Search single file with the given word. Return list of Results or None.
        :param file: String of path of .pdf.
        :param word: Word to be crawled.
        :return: List of matches (String).
        """
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

    def crawl_files(self, path: str, word: str) -> list:
        """
        Crawl directory full of pdf files.
        :param path: Path of file folder.
        :param word: Word to be crawled.
        :return: List of all matches.
        """
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

    @staticmethod
    def save_results(path: str, results: str) -> None:
        """
        Save results to .txt file.
        :param path: Path to save file.
        :param results: All results.
        :return: 
        """
        if path[0] and results:
            with open(file=path[0], mode="w", encoding='utf-8') as f:
                f.write(results)
        else:
            raise NoResults("No results to save!")


if __name__ == '__main__':
    print(__file__)
