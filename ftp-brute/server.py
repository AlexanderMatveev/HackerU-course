from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/Users/alex/Documents/HackerU/ftp", perm="elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer
handler.auth_failed_timeout = 0
handler.banner = "Hello"

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
