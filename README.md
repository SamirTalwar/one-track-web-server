# One Track Web Server

Sometimes you just need a web server that runs the same command over and over again.

I wrote this as a server to dump log files to a web page so that people could iterate quickly. It's been generalised a bit.

## Running

Simple enough. Just use Docker:

    docker run -p <port>:80 -it samirtalwar/one-track-web-server <your command>

For example, if you want to serve up a file located at `/my/directory/file`:

    docker run -v /my/directory/file:/data/file -p 80:80 -it samirtalwar/one-track-web-server cat /data/file

Or generate a random number:

    docker run --rm -it -p 80:80 samirtalwar/one-track-web-server python -c 'import random; print("Your random number is {}!".format(random.randint(1, 100)))'

Then just head to *http://<your Docker host>/* to see the results.

## Building

    make build

## Testing

    make check
