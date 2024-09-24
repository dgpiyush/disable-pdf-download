from http.server import BaseHTTPRequestHandler, HTTPServer

class StaticServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if sendReply == True:
                f = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(bytes(f,'utf-8'))
        except:
            self.send_error(404,'File Not Found: %s' % self.path)

def run():
    webServer = HTTPServer(("", 8080), StaticServer)
    print("Server started http://localhost:8080")

    try:
        webServer.serve_forever()
    except:
        webServer.socket.close()

run()
