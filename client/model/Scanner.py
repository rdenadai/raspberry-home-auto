# -*- coding: utf-8 -*-


import logging
import subprocess
from subprocess import PIPE, STDOUT, DEVNULL
import time
import uuid
from multiprocessing import cpu_count, Pool

import nmap


# Information:
# https://bitbucket.org/xael/python-nmap
# https://nmap.org/book/man-briefoptions.htmls


def scan_active_ips(ip_address):
    try:
        fping = subprocess.call(
            ["fping", "-c1", "-b1", "-t200", ip_address],
            stdin=PIPE, stdout=DEVNULL, stderr=STDOUT
        )
        if fping == 0:
            return ip_address
    except Exception as e:
        logging.error(str(e))
    return None


def scan_active_host(host):
    try:
        nm = nmap.PortScanner()
        nm.scan(host, arguments='-n -O -sN -PE --min-rate 5000', sudo=True)
        return nm[host]
    except Exception as e:
        logging.error(str(e))
    return None


class NetworkScanner():

    def __init__(self):
        self.data = []
        self.running = False

    def scan(self):
        self.data = []
        self.running = True
        ips_address = []
        for ip_address in range(0, 255):
            ips_address.append('192.168.0.%s' % (str(ip_address)))

        num_consumers = cpu_count() * 4

        # Process fping command
        pool_fping = Pool(processes=num_consumers)
        active_hosts = list(filter(None.__ne__,
                            set(pool_fping.map(scan_active_ips, ips_address))))
        pool_fping.close()
        pool_fping.join()

        # Process nmap command!
        pool_nmap = Pool(processes=num_consumers)
        hosts_list = list(filter(None.__ne__, set(pool_nmap.map(scan_active_host, active_hosts))))
        pool_nmap.close()
        pool_nmap.join()

        # Run the list of hosts to generate data!
        for host in hosts_list:
            hostname = host.hostname()
            state = host.state()
            ipv4 = host['addresses']['ipv4']
            mac = ''
            vendor = ''
            if host['vendor']:
                mac = host['addresses']['mac']
                vendor = host['vendor'][mac]

            self.data.append({
                'uuid': str(uuid.uuid4()),
                'hostname': hostname,
                'state': state,
                'ipv4': ipv4,
                'mac': mac,
                'vendor': vendor,
                'time': int(time.time())
            })
        self.running = False
