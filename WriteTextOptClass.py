from config import MAX_BUFFER


class WriteTextOpt(object):
    """this class is used for reducing the I/O operation

    """

    def __init__(self, max_buffer: int=None, suffix: str='\n'):
        self.buffer = []
        self.path = ''
        self.suffix = suffix
        if max_buffer is not None:
            self.max_buffer = max_buffer
        else:
            self.max_buffer = MAX_BUFFER

    def get(line: str, path: str=None, flush: bool=False):
        if path is not None:

        else:
            if

    def flush():
        if len(self.buffer) > 0:
            self.write_batch()

    def write_batch(path: str=None):
        """
        """
        if path is None:
            path = self.path

        if path is None or self.is_empty():
            return

        with open(path, 'a+') as f:
            for line in self.buffer:
                f.write(line + self.suffix)

    def is_empty():
        return len(self.buffer) == 0

    def is_full():
        return len(self.buffer) >= self.max_buffer
