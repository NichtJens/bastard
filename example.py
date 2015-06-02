#!/usr/bin/env python

from bastard import recognized


class A(object):
    def f(self):
        print 'A.f'

@recognized
class B(A):
    def f(self):
        self.parent.f()
        print 'B.f'


B().f()


