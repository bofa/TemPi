'''
Created on Jun 7, 2015

@author: tobimag
'''

#from ABE_ADCDACPi import ADCDACPi
from config import ADConverterSettings

class ADConverter:
    
    def __init__(self):
        if(ADConverterSettings.useRealAD):
            print "Real AD not activated"
            #self.adcdac = ADCDACPi()
            #self.adcdac.set_adc_refvoltage(3.3)
        else:
            self.file = open("offline_measurements.txt")
            self.index = 0
            self.measurements = []
            for line in self.file:
                self.measurements.append(line)
    
    def getMeasurement(self):
        """
        Returns the latest voltage measurement
        """
        if(ADConverterSettings.useRealAD):
            print "Real AD not activated"
            #return self.adcdac.read_adc_voltage(1)
        else:
            return self.__readMeasurementFromFile()
    
    def __readMeasurementFromFile(self):
        measurement = self.measurements[self.index]
        self.index = self.index + 1
        return measurement
    