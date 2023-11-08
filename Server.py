from data_server import DataServer
from load_server_settings import LoadServerSettings
from http.server import HTTPServer
from http_server import SimpleGetHandler

class Server:
    httpd = None
    server_address = () 

    @staticmethod        
    def run():  
        LoadServerSettings.load(DataServer, "settings/config.json")        
        Server.server_address = (DataServer.APP_HOST, DataServer.APP_PORT)
        Server.httpd = HTTPServer(Server.server_address, SimpleGetHandler)
        Server.httpd.serve_forever()