from http.server import BaseHTTPRequestHandler
hostName = "localhost"
serverPort = 8080

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(
            bytes('<form action="submit()" method="get" target="_blank">', "utf-8"))
        self.wfile.write(
            bytes('<button type="submit" formmethod="post">Submit</button>', "utf-8"))
        self.wfile.write(bytes("</form>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        return
    def do_POST(self):
        print('hello')
