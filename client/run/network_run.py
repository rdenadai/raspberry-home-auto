# -*- coding: utf-8 -*-


import logging
import time
from ..model.Scanner import NetworkScanner


def main():
    ns = NetworkScanner()
    while True:
        if not ns.running:
            logging.warning('-' * 10)
            logging.warning("Networking scan will run...")
            ns.scan()
            logging.warning("Networking goes to sleep for 5 minutes...")
            time.sleep(300)


# Run using: python -m client.run.network_run
if __name__ == '__main__':
    main()
