#!/usr/bin/env python

from bastard import recognized, recognizer


class A(object):
    """The base class"""
    def f(self):
        print 'A.f'


class S(A):
    """A sub class using super()"""
    def f(self):
        super(S, self).f()
        print 'S.f'


@recognized
class B(A):
    """A sub class using self.parent"""
    def f(self):
        self.parent.f()
        print 'B.f'


@recognizer('mother')
class C(A):
    """A sub class using mother as parent name"""
    def f(self):
        self.mother.f()
        print 'C.f'



S().f()
B().f()
C().f()


