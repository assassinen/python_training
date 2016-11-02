__author__ = 'NovikovII'


class BookEntry:
    def __init__(self, **kwargs):
        self.parament = {}
        for key, item in kwargs.items():
            self.parament[key] = item