import SimpleHTTPServer
import SocketServer
import logging
import cgi
import time
import sys
import json
import functions
import loader

if len(sys.argv) > 2:
    PORT = int(sys.argv[2])
    I = sys.argv[1]
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    I = ""
else:
    PORT = 8000
    I = ""

cur_time = (time.strftime("%H:%M:%S"))

feedback = {}
data = {}

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.warning("======= GET STARTED =======")
        logging.warning(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        username = form.list[0].name
        passcode = form.list[0].value

        # Check if the user exists and the password is correct
        if self.check_auth(username, passcode):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            for item in form.list:
                data[item.name] = item.value
                feedback['data'] = data
            for command in form.list:
                print cur_time + "(" + username + ")" + command.name + " => " + command.value
                # Check if command (method) has a permission level and it exists
                if command.name in loader.func_perm:
                    level = loader.func_perm[command.name]
                    # Check if permission level exists
                    if username in loader.permissions:
                        # Last check if user has permissions to call the function
                        if loader.permissions[username] >= level:
                            methodtocall = getattr(functions, command.name)
                            result = methodtocall(command.value)

                            if result:
                                print "calling function" + command.name
                                self.set_feedback("ok", True, "Method returned True")
                            else:
                                print "function returned false"
                                self.set_feedback("ok", False, "Method returned False")
                        else:
                            print "no permissions"
                            self.set_feedback("error", False, "No permissions")
                    else:
                        print "User permission error"
                        self.set_feedback("error", False, "User permission error")
                else:
                    print "Unknown command"
                    self.set_feedback("error", False, "Unknown command" + command.name)
                self.wfile.write(feedback)
                print json.dumps(feedback)
        else:
            print cur_time + " failed to login " + form.list[0].name + form.list[0].value
            feedback['status'] = "error"
            feedback['description'] = "failed to login"
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()


        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def check_auth(self, get_username, get_password):
        if loader.users[get_username] == get_password:
            return True
        else:
            return False

    def set_feedback(self, status, succeeded, description):
        feedback['status'] = status
        feedback['succeeded'] = succeeded
        feedback['description'] = description

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

loader.load_users()
loader.load_methods()

print "Serving at: http://%(interface)s:%(port)s" % dict(interface=I or "localhost", port=PORT)
httpd.serve_forever()