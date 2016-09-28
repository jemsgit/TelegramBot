import re

def getValues(data):
    tempData = re.split(' +', data, maxsplit=1)
    try:
        first = tempData[0]
    except IndexError:
        first = ''
    try:
        second = tempData[1]
    except IndexError:
        second = ''

    return [first, second]
	
def getMultipleValues(data, parts):
    tempData = re.split(' +', data, maxsplit=parts)
    try:
        link = tempData[0]
        isYoutube = tempData[1]
        image = tempData[2]
        title = tempData[3]
    except IndexError:
        first = ''
    return [link, isYoutube, image, title]

class messageParser():

    def parsePhotoData(data): 
        values = getValues(data)
        data = {'photo': values[0], 'message': values[1]}
        return data

    def parseLinkData(data):
        values = getValues(data)
        data = {'link': values[0], 'message': values[1]}
        return data
		
	def parseVideoLinksData(data):
        values = getMultipleValues(data, 3)
        data = {'link': values[0], 'isYoutube' : values[1], 'photo': values[2], 'message': values[3]}
        return data
        
    
