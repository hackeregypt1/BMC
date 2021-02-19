#####################
#      Author:Ahmed-Ezzat     #
#      Get Ip Any Website        #
#####################
import socket

domain = input ("Link The Web:")
ip = ("The Ip Is:")
ip2 = socket.gethostbyname(domain)
ur = ("Ur Local Host:")
ur2 = socket.gethostname()
print (ip+ip2)
print (ur+ur2)
