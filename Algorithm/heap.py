class Heap(object):
    def __init__(self, record):
        self.record = record

    def parent(self, idx):
        return idx/2

    def left(self, idx):
        return 2 * idx

    def right(self, idx):
        return 2 * idx + 1
