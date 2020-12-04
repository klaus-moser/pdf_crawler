from basic_backend import *


class Model:
    """The model that fetches all necessary data from the backend."""

    def __init__(self):
        """Get default path in start up."""
        self.bk = BackendClass()
        observer_a = Observer()
        self.bk.attach(observer_a)
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
