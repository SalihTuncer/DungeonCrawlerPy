class NameNotAllowed(Exception):

    def __init__(self, name):
        self.message = name, ' as a name is not allowed.'
        super().__init__(self.message)
