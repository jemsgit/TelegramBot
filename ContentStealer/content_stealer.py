import vk_mini_api
import time
import random


def randomizeStrings(path):
    content = open(path).readlines()
    content = random.shuffle(content)
    with open(path, 'w') as F:
            F.writelines(f)
            
token = '202ff2809749836e59d4dbba6cfb62d13a317626d0b9a0664aec4341eea2d331b4b8ee285d610f0cb465c'
community_id = '48369111'
exclude = ['Logo pictures', '#Stuff We Like']
vk_api = vk_mini_api.Session(token);
albums = vk_api.getCommunityAlbums({'owner_id':community_id})
albums_id = []
for element in albums:
    if element['title'] not in exclude:
        albums_id.append({'id': element['aid'], 'title': element['title']})
for id_element in albums_id:
    photos = vk_api.getPhotos({'owner_id':community_id, 'album_id': id_element['id'], 'photo_sizes': '0'})
    photos_id = []
    title = id_element['title']
    for element in photos:
        if 'src_xxbig' in element:
            link = element['src_xxbig']
        elif 'src_xbig' in element:
            link = element['src_xbig']
        else:
            link = element['src_big']
        photos_id.append(link + ' ' + title)
    with open("content.txt", "a", encoding='utf8', errors = 'ignore') as myfile:
        for item in photos_id:
            myfile.write("%s\n" % item)
    time.sleep(0.4)


