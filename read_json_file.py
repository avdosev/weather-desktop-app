import json

def readJsonFromFile(filename):
    file = open(filename, 'r')
    arr = json.loads(file.read())
    file.close()
    return arr