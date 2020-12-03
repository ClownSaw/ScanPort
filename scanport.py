#!/usr/bin/python3
#Autor: ClownSaw
#Web: www.clownsaw.tk
"""!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!    !!!!!!!!!!!!!!!!!    !!!!    !!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
import argparse, os, sys, random, time
import socket # for connecting
from colorama import init, Fore

from threading import Thread, Lock
from queue import Queue

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()

def ClownLogo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

  .----. .---.   .--.  .-. .-.         
 { {__  /  ___} / {} \ |  `| | * # +        
 .-._} }\     }/  /\  \| |\  |   + * #     
 `----'  `---' `-'  `-'`-' `-' + # *       
    * + # .----.  .----. .----.  .---. 
  * + #   | {}  }/  {}  \| {}  }{_   _}
    # + * | .--' \      /| .-. \  | |  
  * + +   `-'     `----' `-' `-'  `-'  
                   Autor: ClownSaw
"""
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

ClownLogo()

clown1 = "HOST/IP"
clown2 = "PORT"
clown3 = "STATE"
clown4 = "SERVICE"

common_ports={21:'ftp',22:'ssh',23:'telnet',25:'smtp',53:'dns',135:'NetBios',139:'NetBios',110:'POP3',143:'imap',119:'nntp',389:'LDAP',8080:'proxy web', 443:'secure http', 9418:'git', 80:'http'}

# number of threads, feel free to tune this parameter as you wish
N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()

print(f"  {clown1:14} {clown2:9} {clown3:6} {clown4:5}")
def port_scan(worker):
    """
    Scan a port on the global variable `host`
    """
    try:
        s = socket.socket()
        s.connect((host, worker))
    except:
        with print_lock:
            print(f"{GRAY}{host:13}:{worker:5} is closed  {RESET}", end='\r')
    else:
        with print_lock:
            print(f"{GREEN}{host:13}: {worker:5}/tcp   open   {common_ports[worker]}{RESET}")
    finally:
        s.close()


def scan_thread():
    global q
    while True:
        # get the port number from the queue
        worker = q.get()
        # scan that port number
        port_scan(worker)
        # tells the queue that the scanning for that port 
        # is done
        q.task_done()


def main(host, common_ports):
    global q
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon = True
        # start the daemon thread
        t.start()

    for worker in common_ports:
        # for each port, put that port into the queue
        # to start scanning
        q.put(worker)
    
    # wait the threads ( port scanners ) to finish
    q.join()


if __name__ == "__main__":
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Simple scan port")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, common_ports)
