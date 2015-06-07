'''
Created on Jun 7, 2015

@author: tobimag
'''

from firebase import firebase
from datetime import datetime
from config import FirebaseStrings

class Server:
    
    def __init__(self, user=FirebaseStrings.user):
        self.firebase = firebase.FirebaseApplication(FirebaseStrings.url)
        self.user = user
    
    def putEstimationData(self, currentTemp, estimatedTimeRemaining):
        timestamp = str(datetime.now().time())
        newData = {FirebaseStrings.timeStamp: timestamp, 
                   FirebaseStrings.temperature: currentTemp, 
                   FirebaseStrings.timeLeft: estimatedTimeRemaining}
        self.firebase.put(self.user, FirebaseStrings.latestPost, newData)
        