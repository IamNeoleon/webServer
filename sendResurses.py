from http.server import BaseHTTPRequestHandler
from genericpath import exists
import helper

class SendResurses(BaseHTTPRequestHandler):
    def sendHeaders(self, code):
        self.send_response(code)
        self.end_headers()


    def renderPage(self, page):
        self.sendHeaders(200)
        self.wfile.write(page.encode('utf-8'))


    def getContent(self, path):
        if exists(path[1:]):
            self.sendHeaders(200)
            self.wfile.write(helper.read_file(path[1:]))