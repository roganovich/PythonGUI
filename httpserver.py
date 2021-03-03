import http.server

SERVER_ADRESS = ('localhost', 3636)
SERVER_HANDLER = http.server.CGIHTTPRequestHandler

http = http.server.HTTPServer(SERVER_ADRESS, SERVER_HANDLER)
http.serve_forever()