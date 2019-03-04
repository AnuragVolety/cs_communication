###### client program for A

import socket
import json               
def send(message,port): 
# Create a socket object
	s = socket.socket()         	 
	#port = 12341 for A 12342 for B 12343 for C and 12344 for D
	#port = {"A":12341,"B":12342,"C":12343,"D":12344}
	s.connect(('127.0.0.1', port))
	s.send(message.encode())
	s.close() 

if __name__ == '__main__':
	import sys
	flag = True
	message = sys.argv[1]
	sender = sys.argv[2]
	receiver = sys.argv[3]
	if sender=='1':
		port = 12341
	if sender=='2':
		port = 12342
	if sender=='3':
		port = 12343
	if sender=='4':
		port = 12344
	if sender=='5':
		port = 12345
	if sender=='6':
		port = 12346
	if sender=='7':
		port = 12347

		"""print ("POSSIBLE PATHS:")
		if reciever == "2":
			print ("1 Hops; A - B")
		elif reciever == "3":
			print ("1 Hops;  B - C")	
			print ("2 Hops;  B - D - C")
		elif reciever == "4":
			print ("2 Hops; A - B - D")	
			print ("3 Hops; A - B - C - D")			
		port = 12342
	elif sender=='3':
		print ("POSSIBLE PATHS:")
		if reciever =='2':
			print ("1 Hops; C - B")	
			print ("2 Hops; C - D - B")
			port = 12342
		elif reciever =='1':
			print ("2 Hops; C - B - A")	
			print ("3 Hops; C - D - B - A")
			port = 12342	
		elif reciever == '4':
			print ("2 Hops; C - B - D")	
			print ("1 Hops; C - D")
			port = 12344		
	elif sender=='2':
		print ("POSSIBLE PATHS:")
		if reciever=='1':
			print ("1 Hops; B - A")	
			port = 12341
		elif reciever=='3':
			print ("2 Hops; B - D - C")	
			print ("1 Hops; B - C")
			port = 12343
		elif reciever=='4':
			print ("2 Hops; B - C - D")	
			print ("1 Hops; B - D")
			port = 12344
		else:
			flag=False
			print('invalid receiver')
	elif sender=='4':
		print ("POSSIBLE PATHS:")
		if reciever =='2':
			port = 12342
			print ("2 Hops; D - C - B")	
			print ("1 Hops; D - B")
		elif reciever =='1':
			port = 12342
			print ("2 Hops; D - B - A")	
			print ("3 Hops; D - C - B- A")
		elif reciever == '3':
			print ("2 Hops; D - B - C")	
			print ("1 Hops; D - C")
			port = 12343				
	else:
		flag=False
		print('invalid receiver')
		"""
	if flag:
		d = {'data':message , 'receiver':receiver,'sender':sender,'path':sender,'pathFound':'0','pole':'0'}
		data = json.dumps(d)
		print(data)
		send(data,port) 
