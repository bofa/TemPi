'''
Created on Jun 7, 2015

@author: tobimag
'''

from ABE_ADCDACPi import ADCDACPi
from config import ADConverter

class ad:
    
    def __init__(self):
        if(ADConverter.useRealAD):
            self.adcdac = ADCDACPi()
            self.adcdac.set_adc_refvoltage(3.3)
        #else
            # open file for reading
    
    def getMeasurement(self):
        if(ADConverter.useRealAD):
            return self.adcdac.read_adc_voltage(1)
        else:
            return __readMeasurementFromFile()
    
    def __readMeasurementFromFile(self):
        return 0;