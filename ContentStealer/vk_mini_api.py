# -*- coding: UTF-8 -*-
import urllib.request, json, sys
import requests

class Session(object):
    """docstring fos Vk_API"""
    def __init__(self, token):
        self.token = token
        self.url  = u'https://api.vk.com/method/'
        
 
    def getPhotos(self, params):
        methodName = 'photos.get'
        paramsString = 'access_token=%s&owner_id=-%s&album_id=%s&photo_sizes%s' %(self.token, params['owner_id'], params['album_id'], params['photo_sizes'])
        response = self.sendRequest(methodName, paramsString)
        return response

    def getCommunityAlbums(self, params):
        methodName = 'photos.getAlbums'
        paramsString = 'access_token=%s&owner_id=-%s' %(self.token, params['owner_id'])

        response = self.sendRequest(methodName, paramsString)
        return response
    
    def sendRequest(self, methodName, paramsString):
        url = self.url + methodName
        paramsString = paramsString.encode('utf-8')
        req = urllib.request.Request(url, data = paramsString, headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))

        if 'error' in data:
            print (data)
            return list()
        return data[u'response']

        