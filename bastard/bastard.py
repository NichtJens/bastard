
def recognized(cls, parent="parent"):
    setattr(cls, parent, property(lambda self: super(cls, self)))
    return cls


class recognizer(object):

    def __init__(self, parent):
        self.parent = parent

    def __call__(self, cls):
        return recognized(cls, self.parent)


