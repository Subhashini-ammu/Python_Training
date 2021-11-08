import unittest
from gtn import check


class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(check(1, 1, 1), 1)

    def test2(self):
        self.assertEqual(check(5, 3, 2), 5)

    def test3(self):
        self.assertEqual(check(3, 10, 5), 10)

    def test4(self):
        self.assertEqual(check(0, 0, 4), 4)

    def test5(self):
        self.assertEqual(check(0.9, 2, 6), 6)

    def test6(self):
        self.assertEqual(check(1.5, 1.5, 3.6), 3.6)

    def test7(self):
        self.assertEqual(check(-2.3, 2.5, 2.5), 2.5)

    def test8(self):
        self.assertEqual(check(-18, -30, -18), -18)

    def test9(self):
        self.assertEqual(check(-10.2, 11.2, -10.2), 11.2)

    def test10(self):
        self.assertEqual(check("ammu", 11, 1), "error")
