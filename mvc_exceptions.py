"""File that holds all self-made exceptions."""


class ItemAlreadyStored(Exception):
    pass


class ItemNotStored(Exception):
    pass


class NoResults(Exception):
    pass


class NoPdfFilesFound(Exception):
    pass


class NoDefaultPathSet(Exception):
    pass


class FileDialogError(Exception):
    pass


class ErrorCrawlingFile(Exception):
    pass


if __name__ == "__main__":
    print(__file__)
