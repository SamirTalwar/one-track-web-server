#!/usr/bin/env python

import argparse
from http import HTTPStatus
import http.server
import signal
import subprocess
import threading


DEFAULT_PORT = 80


class Server:
    def __init__(self, command, port):
        self.command = command
        self.port = port

    def start(self):
        handler = self._handler()
        self.http_server = http.server.HTTPServer(('', self.port), handler)
        try:
            self.http_server.serve_forever()
        except KeyboardInterrupt:
            pass

    def stop(self):
        self.http_server.shutdown()

    def _handler(self):
        command = self.command

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path != '/':
                    self.send_error(HTTPStatus.NOT_FOUND)

                self.send_response(HTTPStatus.OK)
                self.end_headers()
                subprocess.run(command, stdout=self.wfile, stderr=self.wfile)

        return Handler


def run(command, port):
    server = Server(command, port)
    threading.Thread(target=server.start).start()
    signal.signal(signal.SIGTERM, lambda signum, frame: server.stop())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='One-track web server.')
    parser.add_argument(
            'command', type=str, nargs=argparse.REMAINDER,
            help='the command to run (e.g. `echo "Hello, World!"`)')
    parser.add_argument(
            '-p', '--port', type=int, default=DEFAULT_PORT,
            help='the web server port')
    args = parser.parse_args()
    run(args.command, args.port)
