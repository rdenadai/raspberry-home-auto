# -*- coding: utf-8 -*-

import nmap
import subprocess
import sys
from multiprocessing import cpu_count, Pool, Process, Queue
from socket import *


# Information:
# https://bitbucket.org/xael/python-nmap
# https://nmap.org/book/man-briefoptions.htmls


def scan_active_ips(ip_address):
    active_hosts = []
    fping = subprocess.call(
        ["fping", "-c1", "-b1", "-t200", ip_address]
    )
    if fping == 0:
        return ip_address
    return None


def scan_active_host(host):
    nm = nmap.PortScanner()
    nm.scan(host, arguments='-n -O -sN -PE --min-rate 5000', sudo=True)
    return nm[host]


class NetworkScanner():

    def __init__(self):
        self.data = []
        self.running = False

    def scan(self):
        self.running = True
        ips_address = []
        for ip_address in range(0, 255):
            ips_address.append(f'192.168.0.{ip_address}')

        num_consumers = cpu_count() * 4
        pool_fping = Pool(processes=num_consumers)
        active_hosts = list(filter(None.__ne__,
                            set(pool_fping.map(scan_active_ips, ips_address))))

        pool_nmap = Pool(processes=num_consumers)
        hosts_list = pool_nmap.map(scan_active_host, active_hosts)
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
                'hostname': hostname,
                'state': state,
                'ipv4': ipv4,
                'mac': mac,
                'vendor': vendor
            })
        self.running = False
