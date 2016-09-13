import requests
import urllib.request

class requestManager(object):


    def __init__(self, host):
        super(requestManager, self).__init__()
        self.disable_web_page_preview = 'false'
        self.host = host
		
    def sendPost(self, channel_id, message):
        url = self.host + "sendMessage"
        r = requests.post(url, data={"chat_id": channel_id, 'text': message, 'disable_web_page_preview': self.disable_web_page_preview})

    def sendPhoto(self, channel_id, photoPath, message):
        url = self.host + "sendPhoto"
        r = requests.post(url, data={"chat_id": channel_id, 'caption': message}, files = {'photo': open(photoPath, 'rb')})

    def downloadPhoto(self, url, name):
        path = name +".jpg"
        urllib.request.urlretrieve(url, path)
        return path
        t
            
        return path

    def checkValidSource(self, url):
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            if response.code < 400:
                valid = True
        except urllib.error.URLError as e:
            valid = False
        except ValueError:
            valid = False
        return valid