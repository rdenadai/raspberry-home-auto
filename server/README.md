### About

This is the code for the server!

It's a simple Progressive Web App, with the background provided by uwsgi and Flask.

P.S.: Python 3 support only...

### Installation

- Download the repository:
> git clone https://github.com/rdenadai/raspberry-home-auto.git

- Please create a virtualenv first:
> $ virtualenv venv
> $ pip install requirements.txt

- Startup
> $ uwsgi --http 0.0.0.0:8181 -w wsgi --wsgi-disable-file-wrapper --async 10 --ugreen --processes 4 --enable-threads
