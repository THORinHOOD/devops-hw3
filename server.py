# from flask import Flask, request, send_from_directory, make_response
# from datetime import date

# app = Flask(__name__, static_url_path='/', static_folder='')

# @app.route('/', methods=['GET'])
# def index():
#     today = date.today()
#     return "Today : " + str(today) + "</br> Browser fingerprint : " + str(request.headers['User-Agent'])

# if __name__ == "__main__":
#     app.run()

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import date

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self):
        today = date.today()
        content = "<html><body><div>" + str(today) + "</div><div>" + self.headers['User-Agent'] + "</div></body></html>"
        return content.encode("utf8")

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html())

if __name__ == "__main__":
    server_address = ("192.168.33.20", 80)
    httpd = HTTPServer(server_address, S)
    print("Starting httpd server on " + server_address[0] + ":" + str(server_address[1]))
    httpd.serve_forever()
