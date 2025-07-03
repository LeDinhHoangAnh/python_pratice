# logger_module.py

from datetime import datetime

# Context Manager write log into file
class LogWriter:
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        self.file = open(self.filepath, "a", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Decorator to log function
def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log = f"{datetime.now()} | {func.__name__}({args}) = {result}\n"
        with LogWriter("operation.log") as f:
            f.write(log)
        return result
    return wrapper
