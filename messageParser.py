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

class messageParser():

    def parsePhotoData(data): 
        values = getValues(data)
        data = {'photo': values[0], 'message': values[1]}
        return data

    def parseLinkData(data):
        values = getValues(data)
        data = {'link': values[0], 'message': values[1]}
        return data
        
    
