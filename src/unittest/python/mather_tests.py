import sys, os
import imp
from pybuilder_nose import mathClass
import unittest

class FoobarTests(unittest.TestCase):
  
  def test_foobar(self):
    t = mathClass.Mather(1,1)

    self.assertEquals(t.add(), 2)
    self.assertEquals(t.div(), 1.0)
    self.assertEquals(t.mul(), 1)
    self.assertEquals(t.sub(), 0)


