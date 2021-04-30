#!/usr/bin/python3

from pyfiglet import Figlet
import socket
import subprocess
import sys

# BY BH94 HACK THE PLANET




subprocess.call("clear",shell=True)

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Pscanner!!!'))




print("\n")


try:
	host = input("\nSET THE IP OR URL ADDRESS ===> ")
	for port in range(21,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if s.connect_ex((host, port)):
		   s.close()
		else:
			print("\nport:",port,"on host:",host,"is [OPEN]")

	

except KeyboardInterrupt:

	print("\nTHE PROCESS WAS INTERRUPTED ")
	sys.exit()

except socket.gaierror:
	sys.exit()



except socket.error:
	sys.exit()
