'''
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



'''

import unittest
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("testing").getOrCreate()
sc = spark.sparkContext
print(sc)

# help(spark)
print(dir(spark))
print(spark)


class TestCaseDemo(unittest.TestCase):
    def test_bac(self):
        print("test_bac testing method")

    def test_cba(self):
        print("test_cba testing method")

    def test_abc(self):
        print("test_abc testing method")


unittest.main()
