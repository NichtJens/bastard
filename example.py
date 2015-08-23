#!/usr/bin/env python

from bastard import recognized


class A(object):
    def f(self):
        print 'A.f'


class S(A):
    def f(self):
        super(S, self).f()
        print 'S.f'


@recognized
class B(A):
    def f(self):
        self.parent.f()
        print 'B.f'



S().f()
B().f()


