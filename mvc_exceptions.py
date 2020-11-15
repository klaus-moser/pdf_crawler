# mvc_exceptions.py
class ItemAlreadyStored(Exception):
    pass


class ItemNotStored(Exception):
    pass


class NoResults(Exception):
    pass


class MoPdfFilesFound(Exception):
    pass


class NoDefaultPathSet(Exception):
    pass


if __name__ == "__main__":
    print(__file__)
