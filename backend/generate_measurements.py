'''
Created on Jun 7, 2015

@author: tobimag
'''

import math
import random

numberOfValues = 3600
ovenTemperature = 150
initialBodyTemperature = 20
heatTransferConstant = 0.0002
sigma = 0.01

for index in range(numberOfValues):
    actual = (initialBodyTemperature - ovenTemperature)*math.exp(-index*heatTransferConstant) + ovenTemperature
    noise = random.gauss(0, sigma)
    print actual + noise