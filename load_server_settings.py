import json
import dataBaseManager

class LoadServerSettings:
    @staticmethod
    def load(objectIn, file_settings):
        with open(file_settings) as json_file:
            data = json.load(json_file)
        
            objectIn.APP_HOST = data['APP_HOST']
            objectIn.APP_PORT = int(data['APP_PORT'])
            objectIn.PATH_DB = data['PATH_DB']

            dataBaseManager.DataBaseManager.setPath(objectIn.PATH_DB)
