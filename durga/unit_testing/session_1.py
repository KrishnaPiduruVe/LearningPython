import unittest

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass method execution")

    def setUp (self):
        print("setUp method execution")

    '''
    test method name is not fixed but should be prefixed with test 
    '''
    def test_method1(self):
        print("test_method1 method execution")
    
    def test_method2(self):
        print("test_method2 method execution")
    
    def test_method3(self):
        print("test_method3 method execution")
        print(10/0)

    def tearDown(self):
        print("tearDown method execution")
    
    def test_method4(self):
        print("test_method4 method execution")
        print(10/0)
    
    @classmethod
    def tearDownClass(cls):
        print("tearDown class method executed")

unittest.main()

'''
setup() : open chrome browser
test1() : test login functionality in chrome browser
tearDown() : close chrome browser

setup() : open firefox browser
test2() : test login functionality in firefox browser
tearDown() : close firefox browser

setUpClass(cls) --- > class level method
test1 : test login functionality in chrome browser with valid user name and password
test2 : test login functionality in chrome browser with invalid user name and password
tearDownClass(cls) --- > class level method


10 test methods

setUp() --> 10 times
tearDown() ---> 10 times 
setUpClass(cls) ---> 1 time  
tearDownClass(cls) ---> 1 time 


'''