from firebase import firebase
from datetime import datetime

class Server:
    
    def __init__(self):
        self.serverUrl = "https://shining-heat-5196.firebaseio.com"
        self.user = "tobias"
        self.latest_post = "latest_post"
        self.firebase = firebase.FirebaseApplication(self.serverUrl);
    
    def putData(self, currentTemp, estimatedTimeRemaining):
        timestamp = str(datetime.now().time())
        newData = {'time_stamp': timestamp, 'temp': currentTemp, 'time_left': estimatedTimeRemaining}
        self.firebase.put(self.user, self.latest_post, newData)
        