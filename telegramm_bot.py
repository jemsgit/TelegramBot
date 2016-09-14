from fileManager import fileManager
from requestManager import requestManager
from messageParser import messageParser
from constants import constants
import schedule
import time

host = "https://api.telegram.org/bot" + constants.bot_token + "/"

settingsPath = 'settings.json'

fileManager = fileManager()
channel_dict = fileManager.getSettingsFromFile(settingsPath)
requestManager = requestManager(host)

for key in channel_dict:
    settings = channel_dict.get(key)
    times = settings.get('times')
    print(key)

    def getPostFunction(key, settings):
        def post():
            data = fileManager.getPostData(key)
            if data != None:
                if(settings.get('type') == constants.channel_photo_type):

                    data = messageParser.parsePhotoData(data)
                    valid = requestManager.checkValidSource(data.get('photo'))

                    if valid:
                        filePath = requestManager.downloadPhoto(data.get('photo'), key)
                        request = requestManager.sendPhoto(key, filePath, data.get('message'))
                        fileManager.deleteFile(filePath)
                    else:
                        print('wrong source url')

                else:
                    if(settings.get('type') == constants.channel_links_type):

                        data = messageParser.parseLinkData(data)
                        valid = requestManager.checkValidSource(data.get('link'))

                        if valid:
                            request = requestManager.sendPost(key, data.get('message') + ' ' + data.get('link'))
                        else:
                            print('wrong source url')
        return post
        
    post = getPostFunction(key, settings)

    for t in times:
        print(t)
        schedule.every().day.at(t).do(post)


while 1:
    schedule.run_pending()
    time.sleep(1)