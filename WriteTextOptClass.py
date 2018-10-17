from config import MAX_BUFFER


class WriteTextOpt(object):
    """
    this class is used for reducing the I/O operation
    """

    def __init__(self, max_buffer: int=None, suffix: str='\n'):
        self.buffer = []
        self.path = ''
        self.max_buffer = max_buffer if max_buffer is not None else MAX_BUFFER
        self.suffix = suffix

    def get(line: str, path: str=None):
        """
        """
        if path is not None:
            if path != self.path:
                self.flush()
            self.path = path
        self.buffer.append(line)

    def flush():
        """
        """
        if len(self.buffer) > 0:
            self.write_batch()
        self.buffer = []

    def write_batch(path: str=None):
        """
        """
        if path is None:
            path = self.path

        if path is None or self.is_empty():
            return

        try:
            with open(path, 'a+') as f:
                for line in self.buffer:
                    f.write(line + self.suffix)
        except Exception as e:
            # logs should be added here
            pass

    def is_empty():
        """
        """
        return len(self.buffer) == 0

    def is_full():
        """
        """
        return len(self.buffer) >= self.max_buffer
