import requests
import urllib.request

class requestManager(object):

    headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}

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


    def checkValidSource(self, url):
        try:
            req = urllib.request.Request(url, headers = headers)
            response = urllib.request.urlopen(req)
            if response.code < 400:
                valid = True
        except urllib.error.URLError as e:
            valid = False
        except ValueError:
            valid = False
        return valid