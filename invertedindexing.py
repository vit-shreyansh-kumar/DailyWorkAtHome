""" When you want have a faster search you need to switch to inverted indexes. """

class InvertedIndex:
    def __init__(self):
        self.path = None

    def load(self,file_path):
        self.path = file_path

        try:
