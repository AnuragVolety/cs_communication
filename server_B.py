#### server program for B

import socket               
import client_A
import json
# next create a socket object
s = socket.socket()         
print "Socket successfully created"
port = 12342          
s.bind(('', port))        
print "socket binded to %s" %(port)
s.listen(20)
while True:
    c, addr = s.accept()
    d = c.recv(1024).decode()
    data = json.loads(d)
    data1 = json.loads(d)
    data=eval(json.dumps(data1))
    
    if data['pathFound']=='0':
        path_list = [str(x) for x in data['path'].split()]
        if len(path_list)>1 and '2' in path_list:
            print('Packet discarded',path_list,data)
        elif data['receiver']!="2":
            if data['sender']!='2':
                data['path']+=' 2'
            i_msg = json.dumps(data)
            client_A.send(i_msg,12347) 
            client_A.send(i_msg,12341)
            client_A.send(i_msg,12343)

        else:
            path_list = [str(x) for x in data['path'].split()]
            print('Path found' ,path_list)
            data['pathFound']='1'
            data['path']+=' 2'
            i_msg = json.dumps(data)
            if path_list[-1]=='7':
                client_A.send(i_msg,12347)
            elif path_list[-1]=='1':
                client_A.send(i_msg,12341)
            elif path_list[-1]=='3':
                client_A.send(i_msg,12343)
            
            #print('sender '+data['sender'] +' receiver '+data['receiver'] + ' data : '+data['data'])
    else:
        if data['sender']=='2':
            print(' Received the poling packet')
            print(data['path'])
        else:
            path_list = [str(x) for x in data['path'].split()]
            pos = path_list.index('2')
            print(path_list)
            if path_list[pos-1]=='7':
                print('sent to previous 7')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12347)
            elif path_list[pos-1]=='3':
                print('sent to previous 3')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12343)
            elif path_list[pos-1]=='1':
                print('sent to previous 5')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12341)
    c.close()
