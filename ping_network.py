# -*- coding: utf-8 -*-

import subprocess
import ipaddress
import sys
import os

from common import bcolors

def ping_network(network=None):

    if network == None:
        # Prompt the user to input a network address
        if (sys.version_info > (3, 0)):
            net_addr = input(
                "\nEnter a network address in CIDR format (ex.192.168.1.0/24)\n o enter desired ip: ")
        else:
            net_addr = raw_input("\nIntroduce la dirección de red en formato CIDR (ex.192.168.1.0/24)\n o introduce una ip: ")
            net_addr = net_addr.decode('utf-8')

        # Create the network
        try:
            ip_net = ipaddress.ip_network(net_addr, strict=False)
            # print(ip_net)
        except:
            print(
                "\nEl valor " + bcolors.FAIL + net_addr + bcolors.ENDC + " no parece ser un formato de red IPv4 o IPv6\n")
            if (sys.version_info > (3, 0)):
                wait = input("\nPress any key to continue . . .")
            else:
                wait = raw_input("\nPress any key to continue . . .")
            return None

    else:
        net_addr = network

        if (sys.version_info < (3, 0)):
            net_addr = net_addr.decode('utf-8')

        ip_net = ipaddress.ip_network(net_addr, strict=False)
        #print(ip_net)



    # Get all hosts on that network
    all_hosts = list(ip_net.hosts())
    if len(all_hosts) == 0:
        all_hosts.append(net_addr)
    #print(all_hosts)

    # Configure subprocess to hide the console window
    if os.name == 'nt':
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE

    print("")

    # For each IP address in the subnet,
    # run the ping command with subprocess.popen interface
    for i in range(len(all_hosts)):

        if os.name == 'nt':
            output = subprocess.Popen(['ping', '-n', '1', '-w', '5000', str(all_hosts[i])], stdout=subprocess.PIPE,
                                    startupinfo=info).communicate()[0]
        else:
            output = subprocess.Popen(['ping', '-c', '1', '-W', '5', str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0]

        #print(output)
        if "destination host unreachable" in output.decode('utf-8', errors='ignore').lower() or "host de destino inaccesible" in output.decode('utf-8', errors='ignore').lower():
            if network == None:
                print(str(all_hosts[i]) + " : " + bcolors.FAIL + "Offline" + bcolors.ENDC)
            else:
                print("[ " + str(network) + " ] : " + bcolors.FAIL + "Offline" + bcolors.ENDC)
        elif "request timed out" in output.decode('utf-8', errors='ignore').lower() or "tiempo de espera agotado" in output.decode('utf-8', errors='ignore').lower():
            if network == None:
                print(str(all_hosts[i]) + " : " + bcolors.FAIL + "Offline" + bcolors.ENDC)
            else:
                print("[ " + str(network) + " ] : " + bcolors.FAIL + "Offline" + bcolors.ENDC)
        elif "100% loss" in output.decode('utf-8', errors='ignore').lower() or "100% perdidos" in output.decode('utf-8', errors='ignore').lower() or "100% packet loss" in output.decode('utf-8', errors='ignore').lower():
            if network == None:
                print(str(all_hosts[i]) + " : " + bcolors.FAIL + "Offline" + bcolors.ENDC)
            else:
                print("[ " + str(network) + " ] : " + bcolors.FAIL + "Offline" + bcolors.ENDC)
        else:
            if network == None:
                print(str(all_hosts[i]) + " : " + bcolors.OKGREEN + "Online" + bcolors.ENDC)
            else:
                print("[ " + str(network) + " ] : " + bcolors.OKGREEN + "Online" + bcolors.ENDC)
