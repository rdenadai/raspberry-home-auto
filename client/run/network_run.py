# -*- coding: utf-8 -*-


import requests
import logging
import time
from ..model.Scanner import NetworkScanner
from ..configuration import Configuration


def sync_with_server(data):
    r = requests.post(Configuration.SERVER_URI, data=data)
    if r.status_code == 200:
        logging.warning('Networking data send was successfull!')
    else:
        logging.warning('Networking data error!!! Error code: %s' % (str(r.status_code)))


def main():
    ns = NetworkScanner()
    while True:
        if not ns.running:
            logging.warning('-' * 10)
            logging.warning("Networking scan will run...")
            ns.scan()
            logging.warning("Networking send information to server!")
            sync_with_server(ns.registry)
            logging.warning("Networking goes to sleep for 5 minutes...")
            time.sleep(300)


# Run using: python -m client.run.network_run
if __name__ == '__main__':
    main()
