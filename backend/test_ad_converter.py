'''
Created on Jun 7, 2015

@author: tobimag
'''
import unittest
from config import ADConverterSettings
from ad_converter import ADConverter

class Test(unittest.TestCase):


    def testOfflineMeasurements(self):
        ADConverterSettings.useRealAD = False
        adConverter = ADConverter()
        firstMeasurement = adConverter.getMeasurement()
        secondMeasurement = adConverter.getMeasurement()
        self.assertNotEqual(firstMeasurement, secondMeasurement, "First and second measurement should not be equal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()