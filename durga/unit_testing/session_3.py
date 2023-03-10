'''
Test Suite:
============
By using unittest module we can execute a group of testcases ,which is nothing but testsuite


Problems with unittest module:
=================================

module : unittest
class : TestCase
instance methods :
    setUp()
    test()
    tearDown()
class methods :
    setUpClass(cls)
    tearDownClass(cls)

1. Test methods will be executed in alphabetical order only (test_a == > test_b ===> test_c) and 
    it is not possible to customze the order
2. Test results will be displayed to the console only and it is not possible to generate reports.
3. As the part of batch execution (TestSuite), all the methods from the specified test case classes will be executed 
    and it is not possible to specify particular methods.
4. In unit testing only limited setUp and tearDown methods are available
    setUpClass ==> before executing all test methods of a testcase class
    tearDownClass  ===> after executing all test methods of a TestCase class
    setUp() == > before every test method execution
    tearDown() ==> after every test method execution

    If we want to perform any activity before executing testsuite and after executing testsuite,
     unit test frame work doesnt proide any methods


PyTest : FrameWork 
=====================

most commonly used FrameWork for unit testing
advanced version of unittest
built on top of unittest framework

PyTest is not availble by default with python

pip install pytest

PyTest naming rules :
==========================
1. File name must start with or end with 'test'
    test_google_search.py
    google_search_test.py

2. Class Name should start with 'Test'
    TestGoogleSearch
    TestCaseDemo

3. Test method name must start with 'test_'
    test_method1()
    test_method2()

'''

import unittest


class TestCaseDemo(unittest.TestCase):
    def test_bac(self):
        print("test_bac testing method")

    def test_cba(self):
        print("test_cba testing method")

    def test_abc(self):
        print("test_abc testing method")


unittest.main()
