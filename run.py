#!/usr/bin/env python3
"""FAForever API server

Usage:
  run.py
  run.py [-d | -aio] -p 80
  run.py [-d | -aio] --port=80

Options:
  -h             Show this screen
  -aio           Use aiohttp
  -d             Enable debug mode
  -p --port=<port>  Listen on given port [default: 8080].
"""
import logging
import sys

from docopt import docopt

from api import app, api_init

if __name__ == '__main__':
    args = docopt(__doc__)
    app.config.from_object('config')
    api_init()
    port = int(args.get("--port"))
    print('listen on port {0}'.format(port))
    if args.get('-d'):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        loghandler = logging.StreamHandler(sys.stdout)
        loghandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)-25s - %(levelname)-5s - %(message)s')
        loghandler.setFormatter(formatter)
        root.addHandler(loghandler)

        app.debug = True
        app.run(host='0.0.0.0', port=port)
    else:
        print('with aiohttp')
        from aiohttp_wsgi import serve
        from concurrent.futures import ThreadPoolExecutor

        with ThreadPoolExecutor(max_workers=1) as executor:
            serve(app, executor=executor, port=port)
