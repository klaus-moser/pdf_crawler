#!/usr/bin/env python3

# Filename: model.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This is the model."""

from basic_backend import *


class Model:
    """The model that fetches all necessary data from the backend."""

    def __init__(self, view: object) -> None:
        """
        Get default path in start up.
        :param view: View object.
        """
        self.bk = BackendClass(view)
        self.search_path = self.bk.get_default_path()

    def get_info_text(self) -> str:
        """
        Returns the info text.
        :return: String of info text.
        """
        return self.bk.get_info_text()

    def set_default_path(self, path: str) -> None:
        """
        Set current path as default path.
        :param path: String of path.
        :return:
        """
        self.bk.set_default_path(path=path)

    def get_home_dir(self) -> str:
        """
        Return the home directory of the system.
        :return: String of home dir.
        """
        return self.bk.get_home_dir()

    def crawl_file(self, pdf: str, word: str) -> str:
        """
        Crawl a single pdf file.
        :param pdf: String of file-path.
        :param word: String of the word.
        :return: Result string.
        """
        return self.bk.crawl_file(pdf, word)

    def crawl_files(self, path: str, word: str) -> str:
        """
        Crawl a directory full of pdf files.
        :param path: String of directory of files.
        :param word: String of the word.
        :return: Result string.
        """
        return self.bk.crawl_files(path, word)

    def save_results(self, path: str, results: str) -> None:
        """
        Save results to .txt file.
        :param path: String of path.
        :param results: String of results.
        :return:
        """
        self.bk.save_results(path, results)

    def delete_log(self) -> None:
        """
        Delete .log file if empty.
        :return:
        """
        # TODO: check delete_log()
        self.bk.delete_log()


if __name__ == '__main__':
    print(__file__)
