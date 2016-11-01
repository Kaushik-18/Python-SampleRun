from TestClass1 import TestPy1


class TestPy2(TestPy1) :
             def __init__(self):
                TestPy1.__init__(self)
                self.hit = "33"

             def printed(self):
                print(self.hit, self.mint)

