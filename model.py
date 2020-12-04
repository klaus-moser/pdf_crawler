#!/usr/bin/env python3

# Filename: model.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This is the model."""

from basic_backend import *


class Model:
    """The model that fetches all necessary data from the backend."""

    def __init__(self, view):
        """Get default path in start up."""
        self.bk = BackendClass(view)
        self.search_path = self.bk.get_default_path()

    def get_info_text(self):
        """Returnes the info text."""
        return self.bk.get_info_text()

    def set_default_path(self, path):
        """Set current path as default path."""
        self.bk.set_default_path(path=path)

    def get_home_dir(self):
        """Return the home directory of the system."""
        return self.bk.get_home_dir()

    def crawl_file(self, pdf, word):
        """Crawl a single pdf file."""
        return self.bk.crawl_file(pdf, word)

    def crawl_files(self, path, word):
        """Crawl a directory full of pdf files."""
        return self.bk.crawl_files(path, word)

    def save_results(self, path, results):
        """Save results to .txt file."""
        self.bk.save_results(path, results)

    def delete_log(self):
        """Delete .log file if empty."""
        self.bk.delete_log()


if __name__ == '__main__':
    print(__file__)
