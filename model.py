import basic_backend


class Model:
    """The model that fetches all necessary data from the backend."""

    def __init__(self):
        """Get default path in start up."""
        self.search_path = basic_backend.get_default_path()

    def get_info_text(self):
        """Returnes the info text."""
        return basic_backend.get_info_text()

    def set_default_path(self, path):
        """Set current path as default path."""
        basic_backend.set_default_path(path=path)

    def get_home_dir(self):
        """Return the home directory of the system."""
        return basic_backend.get_home_dir()

    def crawl_file(self, pdf, word):
        """Crawl a single pdf file."""
        return basic_backend.crawl_file(pdf, word)

    def crawl_files(self, path, word):
        """Crawl a directory full of pdf files."""
        return basic_backend.crawl_files(path, word)

    def save_results(self, path, results):
        """Save results to .txt file."""
        basic_backend.save_results(path, results)

    def delete_log(self):
        """Delete .log file if empty."""
        basic_backend.delete_log()


if __name__ == '__main__':
    print(__file__)
