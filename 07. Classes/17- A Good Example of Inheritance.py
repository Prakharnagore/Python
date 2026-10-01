class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self, ):
        self.opened = False

    def open(self):
        if self.opened is False:
            return InvalidOperationError("Stream is not open")
        self.opened = True

    def close(self):
        if self.opened is False:
            return InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


stream = FileStream()
stream.open()
stream.read()
stream.close()
