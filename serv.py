from http.server import HTTPServer, BaseHTTPRequestHandler

from BrightonHoveBusStop import BrightonBusStop
from UKTrainStop import UKTrainStop

numpage = 1
buspage = "File not found"
trainpage = "File not found"

#Page rotation
def prepareHTML():
    global numpage
    global buspage
    global trainpage
    if numpage == 1:
        numpage = 2
        buspage = bus_file.replace("{{{body01}}}",BrightonBusStop("155089")).replace("{{{body02}}}",BrightonBusStop("155070"))
        return buspage
    elif numpage == 2:
        numpage = 3
        trainpage = train_file.replace("{{{body01}}}",UKTrainStop("Moulsecoomb",1)).replace("{{{body02}}}",UKTrainStop("Moulsecoomb",2))
        return trainpage
    elif numpage == 3:
        numpage = 4
        return buspage
    elif numpage == 4:
        numpage = 5
        return trainpage
    elif numpage == 5:
        numpage = 6
        return buspage
    elif numpage == 6:
        numpage = 1
        return trainpage

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        file_to_open = prepareHTML()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

try:
	bus_file = open('bus.html').read()
	train_file = open('train.html').read()
except:
	bus_file = "File not found"
	train_file = "File not found"

#Start http server http://localhost:8080
httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
