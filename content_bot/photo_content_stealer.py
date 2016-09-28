import vk_mini_api
import time
import random
import json
import os.path

with open('photo_settings.json', 'r') as settingsFile:
    communties = json.load(settingsFile)

token = ''
vk_api = vk_mini_api.Session(token);

for key in communties:
    community_id = key
    settings = communties.get(key)
    name = settings.get('name')
    exclude = settings.get('exclude')

    albums = vk_api.getCommunityAlbums({'owner_id':community_id})
    albums_file = name + "_albums.txt"

    if os.path.isfile(albums_file):
        f = open(albums_file, "r", encoding='utf8', errors = 'ignore').readlines()
        while (len(f) > 0):
            exclude.append(f.pop(0))

    albums_id = []
    albums = albums['items']
    for element in albums:
        if element.get('title') not in exclude:
            albums_id.append({'id': element['id'], 'title': element['title']})

    with open(albums_file, "a", encoding='utf8', errors = 'ignore') as myfile:
        for item in albums_id:
            myfile.write("%s\n" % item['title'])

    photos_id = []

    for id_element in albums_id:
        photos = vk_api.getPhotos({'owner_id':community_id, 'album_id': id_element['id'], 'photo_sizes': '1'})
        photos = photos['items']
        title = id_element['title']
        for element in photos:
            sizes = element['sizes']
            link = sizes[-1]['src']
        
            if 'title' in element:
                title = title + ' ' + element['title']
            photos_id.append(link + ' ' + title)
        time.sleep(0.4)

    random.shuffle(photos_id)

    with open(name + ".txt", "a", encoding='utf8', errors = 'ignore') as myfile:
        for item in photos_id:
            myfile.write("%s\n" % item)



