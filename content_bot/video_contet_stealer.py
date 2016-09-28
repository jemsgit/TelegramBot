import vk_mini_api
import time
import random
import json
import os.path

with open('video_settings.json', 'r') as settingsFile:
    communties = json.load(settingsFile)

token = ''
vk_api = vk_mini_api.Session(token);

for key in communties:
    community_id = key
    settings = communties.get(key)
    name = settings.get('name')

    videos = vk_api.getCommunityVideos({'owner_id':community_id, 'count': '200'})
    random.shuffle(videos)

    with open(name + '_videos.txt', 'a', encoding='utf8') as myfile:

        for val in videos:
            element = val
            link = element.get('player')

            isYoutube = False
            if(('youtube' in link)):
                isYoutube = True
            keys = []
            for key in element:
                if 'photo' in key:
                    keys.append(key)
            keys.sort()
            photo = element.get(keys[-1])
            
            myfile.write(link + ' ' + str(isYoutube) + ' ' + str(photo) + ' ' + element.get('title') + '\n')


