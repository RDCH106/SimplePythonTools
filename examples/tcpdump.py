# -*- coding: utf-8 -*-

'''
Example using TCPdump to check online without ping (ICMP)
TCPdump tool sniff the traffic without more traffic overhead
'''

import SimplePythonTools.network.tcpdump as tcpdump
import time
import threading
from SimplePythonTools.network.ping_network import pingNetwork
from SimplePythonTools.common import bcolors
import os

ping_delay = 15  # 15 seconds
offline_threshold = 5  # 5 seconds
refresh_interval = 2  # 2 seconds
execution_lapse = 30  # 30 seconds

if os.name == 'nt':   # Windows
    tcpdump_call = "windump"   # https://www.winpcap.org/windump/
    interface = "1"
else:                 # GNU/Linux
    tcpdump_call = "tcpdump"   # http://www.tcpdump.org/tcpdump_man.html
    interface = "any"

def tcpdump_run():

    tcpd = tcpdump.TCPDump(tcpdump_call=tcpdump_call, interface=interface, traffic_filter="icmp", print_traffic=True)

    def ping_call():
        pingNetwork(network="192.168.1.1", stdout=False)

    th = threading.Timer(interval=ping_delay, function=ping_call)
    th.start()

    tcpd.run()
    status_checker = tcpd.get_status_checker(offline_threshold=offline_threshold)
    print(bcolors.WARNING +
          "\nThe init online status is:"+str(status_checker.is_Online()) +
          "\nThe execution will start in "+str(offline_threshold)+" seconds after first loop execution" +
          "\nRefresh interval: "+str(refresh_interval)+" seconds\n" +
          bcolors.ENDC)
    time.sleep(offline_threshold)

    finish_time = time.time() + execution_lapse
    while finish_time >= time.time():
        time.sleep(refresh_interval)
        if status_checker.is_Online():
            print(bcolors.OKGREEN + "Online" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Offline" + bcolors.ENDC)

    tcpd.stop()

if __name__ == "__main__":
    tcpdump_run()