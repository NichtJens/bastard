
def recognized(cls):
    setattr(cls, 'parent', property(lambda self: super(cls, self)))
    return cls

