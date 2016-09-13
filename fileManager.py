from constants import constants
import os
import json

class fileManager:

    def __init__(self):
        print('create fileManager')

    def getSettingsFromFile(self, settingsPath):
        with open(settingsPath, 'r') as settingsFile:
            self.channel_list = json.load(settingsFile)
        return self.channel_list


    def getPostData(self, key):
        settings = self.channel_list.get(key)
        path = os.path.abspath(settings.get('filePath'))
        postType = settings.get('type')

        f = open(path).readlines()
        message = None
        
        if len(f) == 0:
            print('file ' + path + ' is empty')
            return message

        while (not message) and (len(f) > 0):
            message = f.pop(0);
        
        with open(path, 'w') as F:
            F.writelines(f);

        return message

    def deleteFile(self, filePath):
        os.remove(filePath)


