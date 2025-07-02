# log_reader.py

class LogIterator:
    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        self.file = open(self.filepath, "r", encoding="utf-8")
        return self

    def __next__(self):
        line = self.file.readline()
        if line == "":
            self.file.close()
            raise StopIteration
        return line.strip()
