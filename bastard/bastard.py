
def recognized(cls):
    setattr(cls, 'parent', lambda self: super(cls, self))
    cls.parent = property(cls.parent)
    return cls

