#!/usr/bin/env python

import argparse
from http import HTTPStatus
import http.server
import subprocess


DEFAULT_PORT = 80


def handler(command):
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != '/':
                self.send_error(HTTPStatus.NOT_FOUND)

            self.send_response(HTTPStatus.OK)
            self.end_headers()
            subprocess.run(command, stdout=self.wfile, stderr=self.wfile)

    return Handler


def run(command, port):
    http_server = http.server.HTTPServer(('', port), handler(command))
    http_server.serve_forever()


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
