import unittest


class TestCase2(unittest.TestCase):
    def setUp(self):
        print("TestCase2:setUp")

    def test1(self):
        print("TestCase2:test1")

    def tearDown(self):
        print("TestCase2:tearDown")
