
class Mather(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def add(self):
    return self.a + self.b

  def div(self):
    return float(self.a) / float(self.b)

  def mul(self):
    return self.a * self.b

  def sub(self):
    return self.a - self.b

