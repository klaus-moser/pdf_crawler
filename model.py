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

    def get_all_pdfs_in_folder(self, path):
        """Walk current path for all .pdfs."""
        basic_backend.walk_folder(folder_path=path)

    def delete_log(self):
        """Delete .log file if empty."""
        basic_backend.delete_log()

    def get_home_dir(self):
        """Return the home directory of the system."""
        return basic_backend.get_home_dir()

    def crawl_file(self, pdf, word):
        """Crawl a pdf file."""
        return basic_backend.crawl_pdf_file(pdf, word)

    def walk_folder(self, path):
        """Walk folder and return all the .pdfs"""
        return basic_backend.walk_folder(path)


if __name__ == '__main__':
    print(__file__)
