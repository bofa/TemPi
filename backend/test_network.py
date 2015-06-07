'''
Created on Jun 7, 2015

@author: tobimag
'''
import unittest
from network import Server


class Test(unittest.TestCase):


    def testPutData(self):
        server = Server()
        temp = 34.3
        timeLeft = 78.3
        server.putData(temp, timeLeft)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPut']
    unittest.main()