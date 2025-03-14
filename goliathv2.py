import pyfiglet
import colorama
import socket
import subprocess
import datetime
from datetime import datetime
import sys
import time
import requests
import platform
import scapy
import ipaddress
import os
from scapy.all import IP, ICMP, sr1
import psutil
import json

from colorama import Fore, Back, Style
colorama.init()


def gethelp():
    print()
    print(Fore.YELLOW + '   Available Commands:')
    print('    - scan: Scan a target IP for open ports.')
    print('    - info: Provides info on this program.')
    print('    - scangeo: Geolocates the target IP.')
    print('    - ping: Ping an IP to check if it is reachable.')
    print('    - publicip: Gets your local IP address.')
    print('    - traceroute: Perform a traceroute to an IP or domain.')
    print('    - dns: Perform a DNS lookup on a specified domain.')
    print('    - checkip: Check if the IP address is IPv4 or IPv6')
    print('    - hostname: Get the hostname for an IP address.')
    print('    - sysinfo: Display system information.')
    print('    - logip: Save information for an IP address.')
    print('    - readjson: Reads the logged IP data.')
    print('    - home: Clears the screen and goes back to the home screen.')
    print(Fore.RED + '    - exit: Exit GOLIATH V2.')
    print(Fore.YELLOW)
    getprompt()

def getinfo():
    print()
    print(Fore.YELLOW + '   GOLIATH V2 is a multi-purpose IP toolkit. It is an essential program for')
    print(Fore.YELLOW + '   hackers looking to destroy internet, IPs, or just get information on their')
    print(Fore.YELLOW + '   target! venom and Neuroscopy try to keep this program as affordable and content-')
    print(Fore.YELLOW + '   packed as possible, so that you feel 100% satisfied!')
    print()
    print(Fore.GREEN + '   * If you are using GOLIATH V2 DEMO, we highly recommend you buy the full version for only $14.99!')
    getprompt()

def gethome():
    subprocess.run('cls', shell=True)
    getbanner()

def error():
    print()
    print(Fore.RED + '   Sorry, GOLIATH V2 encountered an error. Did you use a command incorrectly?')
    print('   ' + '~'*74)
    getprompt()

def getprompt():

    print(Fore.LIGHTYELLOW_EX)
    command = input("   > ")

    if command == "help":
        gethelp()

    elif command == "home":
        gethome()

    elif command == "exit":
        exit()

    elif command == "info":
        getinfo()

    elif command == "scan":
        scan()
    
    elif command == "scangeo":
        scangeo()

    elif command == "ping":
        ping()

    elif command == "publicip":
        publicip()

    elif command == "traceroute":
        traceroute()

    elif command == "dns":
        dns()

    elif command == 'checkip':
        checkip()

    elif command == 'hostname':
        hostname()

    elif command == 'sysinfo':
        sysinfo()

    elif command == 'logip':
        logip()

    elif command == 'readjson':
        readjson()

    else:
        error()

    getprompt()

def getbanner():
    print()
    print()
    print(Fore.YELLOW + "        ╔════════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.YELLOW + "        ║                                                                                ║")
    print(Fore.YELLOW + "        ║    ██████╗  ██████╗ ██╗     ██╗ █████╗ ████████╗██╗  ██╗    ██╗   ██╗██████╗   ║")
    print(Fore.YELLOW + "        ║   ██╔════╝ ██╔═══██╗██║     ██║██╔══██╗╚══██╔══╝██║  ██║    ██║   ██║╚════██╗  ║")
    print(Fore.YELLOW + "        ║   ██║  ███╗██║   ██║██║     ██║███████║   ██║   ███████║    ██║   ██║ █████╔╝  ║")
    print(Fore.YELLOW + "        ║   ██║   ██║██║   ██║██║     ██║██╔══██║   ██║   ██╔══██║    ╚██╗ ██╔╝██╔═══╝   ║")
    print(Fore.YELLOW + "        ║   ╚██████╔╝╚██████╔╝███████╗██║██║  ██║   ██║   ██║  ██║     ╚████╔╝ ███████╗  ║")
    print(Fore.YELLOW + "        ║    ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝      ╚═══╝  ╚══════╝  ║")
    print(Fore.YELLOW + "        ║   v0.2.0 - Developed by venom and certifiedfish101                             ║")
    print(Fore.YELLOW + "        ╚════════════════════════════════════════════════════════════════════════════════╝")
    print(Fore.LIGHTYELLOW_EX + "         Type 'help' for a list of commands!")
    print()
    getprompt()

def scan():
    print()
    print('What is the IP you want to scan?')
    target = input(str("Target IP: "))
    print("~" * 50,)
    print("Scanning Target: " + target)
    print("Scanning started at: " + str(datetime.now()))
    print('~'*50)
    
    try:

        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target,port))
            if result == 0:
                print('[*] Port {} is open.'.format(port))
            s.close()

    except KeyboardInterrupt:
        print('\n Exiting')
        input()
        gethome()
    except socket.error:
        print('\n Host not responding')
        getprompt()

def scangeo():
    print()
    print('What is the IP you want to geolocate?')
    target = input(str("Target IP: "))
    print("~" * 50,)
    print("Scanning Target: " + target)
    print("Scanning started at: " + str(datetime.now()))
    print('~'*50)
    try:
        url = f'http://ipinfo.io/{target}/json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            ip = data.get('ip', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            location = data.get('loc', 'N/A')

            print(f'IP Address: {ip}')
            print(f'City: {city}')
            print(f'Region: {region}')
            print(f'Country: {country}')
            print(f'Location (Latitude, Longitude): {location}')
        else:
            print('Error: Unable to fetch geolocation data.')
    
    except Exception as e:
        print(f'An error occurred: {e}')
    
    getprompt()

def ping():
    print()
    print('What is the IP you want to ping?')
    target = input(str("Target IP: "))
    print("~" * 50,)
    print("Pinging Target: " + target)
    print("Pinging started at: " + str(datetime.now()))
    print('~'*50)

    if platform.system().lower() == 'windows':
        command = ['ping', target, "-n", "4"]

    else:
        command = ["ping", target, "-c", "4"]
    
    try:

        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if response.returncode == 0:
            print(f"Ping to {target} was successful.")
            print(response.stdout.decode())
        else:
            print(f"Ping to {target} failed!")
            print(response.stderr.decode())
    
        getprompt()

    except Exception as e:
        print(f"An error occurred while trying to ping {target}: {e}")
    
        getprompt()

def publicip():
    print()
    print("~" * 50,)
    print("Local IP detection started at: " + str(datetime.now()))
    print('~'*50)

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f'Local IP Address: {local_ip}')
    getprompt()

def traceroute():
    max_hops = 100
    print()
    print('What is the IP/Domain destination?')
    destination = input(str("IP/Domain destination: "))
    print("~" * 50,)
    print("Finding traceroute of: " + destination)
    print("Traceroute started at: " + str(datetime.now()))
    print('~'*50)

    print(f"Tracerouting to {destination}...")
    
    for ttl in range(1, max_hops+1):
        # Send an ICMP Echo Request packet with the TTL value
        pkt = IP(dst=destination, ttl=ttl) / ICMP()
        reply = sr1(pkt, timeout=5, verbose=0)
        
        if reply is None:
            print(f"{ttl}: Request Timed Out")
        elif reply.type == 0:
            print(f"{ttl}: {reply.src} (Destination reached)")
            break
        else:
            print(f"{ttl}: {reply.src}")

    getprompt()

def dns():
    print()
    print('Please specify the domain.')
    domain = input(str("Domain: "))
    print("~" * 50,)
    print("DNS lookup started on: " + domain)
    print("DNS lookup started at: " + str(datetime.now()))
    print('~'*50)

    try:
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is: {ip_address}")
    except socket.gaierror:
        print(f"Unable to get the IP address for {domain}")
    
    getprompt()

def checkip():
    print()
    print('Please specifiy the IP to check.')
    ip = input(str("IP address: "))
    print("~" * 50,)
    print("IP check performed on: " + ip)
    print("IP check performed at: " + str(datetime.now()))
    print('~'*50)

    try:
        # Try to create an IPv4 or IPv6 object
        ip_obj = ipaddress.ip_address(ip)
        
        if ip_obj.version == 4:
            print(f"{ip} is an IPv4 address.")
        elif ip_obj.version == 6:
            print(f"{ip} is an IPv6 address.")
    except ValueError:
        print(f"{ip} is not a valid IP address.")

    getprompt()

def hostname():

    print()
    print('Please specify the IP to resolve the hostname.')
    ip = input(str("IP address: "))
    print("~" * 50)
    print("IP to be scanned: " + ip)
    print("Hostname check performed at: " + str(datetime.now()))
    print('~' * 50)

    try:
        # Try to get the hostname for the IP address
        hostname, _, _ = socket.gethostbyaddr(ip)
        print(f"Hostname for IP {ip}: {hostname}")
    except socket.herror:
        # If the hostname cannot be resolved, inform the user
        print(f"Could not resolve hostname for IP {ip}")

def sysinfo():
        # Gather system information in one dictionary
    system_info = {
        'OS': platform.system(),
        'OS Version': platform.version(),
        'OS Release': platform.release(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Logical CPU Cores': psutil.cpu_count(logical=True),
        'Total Memory': f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        'Available Memory': f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
        'Used Memory': f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
        'Memory Usage': f"{psutil.virtual_memory().percent}%",
        'Total Disk Space': f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB",
        'Used Disk Space': f"{psutil.disk_usage('/').used / (1024 ** 3):.2f} GB",
        'Free Disk Space': f"{psutil.disk_usage('/').free / (1024 ** 3):.2f} GB",
        'Disk Usage': f"{psutil.disk_usage('/').percent}%",
    }
    
    # Print all system information
    print("\nSystem Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    sysinfo()

def logip():

    ip = input('IP Address: ')
    geolocation = input('Geolocation: ')
    openports = input('Open ports: ')
    ipv4ipv6 = input('IPv4 or IPv6? ')
    hostname = input('Hostname: ')

    try:
        data = {
            "IP Address": ip,
            "Geolocation": geolocation,
            "Open ports": openports,
            "IP type": ipv4ipv6,
            "Hostname": hostname,
        }

        with open('output.json', 'w') as f:
            json.dump(data, f)

        print()
        print(Fore.LIGHTGREEN_EX + '[*] Data saved successfully!')
        print(Fore.YELLOW)
        with open('output.json') as f:
            outputdata = json.load(f)
            print(outputdata)


    except:
        print(Fore.RED + 'An unknown error occured. Check if you are using')
        print(Fore.RED + 'a cracked or broken verson of GOLIATH V2.')
        getprompt()

def readjson():

    try:

        with open('output.json') as f:
            outputdata = json.load(f)
            print(Fore.YELLOW)
            print(outputdata)
    
    except:

        print(Fore.RED + ' Goliath failed to fetch data from JSON.')
        print(' (Does the file exist?)')
    
    
    getprompt()


gethome()



