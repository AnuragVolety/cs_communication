#### server program for B

import socket               
import client_A
import json
# next create a socket object
s = socket.socket()         
print "Socket successfully created"
port = 12343          
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
        if len(path_list)>1 and '3' in path_list:
            print('Packet discarded',path_list,data)
        elif data['receiver']!="3":
            #print('sender '+data['sender'] +' receiver '+data['receiver'])
            if data['sender']!='3':
                data['path']+=' 3'
            i_msg = json.dumps(data)
            client_A.send(i_msg,12342) 
            client_A.send(i_msg,12344)
        else:
            path_list = [str(x) for x in data['path'].split()]
            print('Path found',path_list)
            data['pathFound']='1'
            data['path']+=' 3'
            i_msg = json.dumps(data)
            if path_list[-1]=='2':
                client_A.send(i_msg,12342)
            elif path_list[-1]=='4':
                client_A.send(i_msg,12344)
            elif path_list[-1]=='5':
                client_A.send(i_msg,12345)
            
            #print('sender '+data['sender'] +' receiver '+data['receiver'] + ' data : '+data['data'])
    else:
        if data['sender']=='3':
            print(' Received the poling packet')
            print(data['path'])
        else:
            path_list = [str(x) for x in data['path'].split()]
            pos = path_list.index('3')
            print(path_list)
            if path_list[pos-1]=='2':
                print('sent to previous 2')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12342)
            elif path_list[pos-1]=='4':
                print('sent to previous 4')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12344)
            elif path_list[pos-1]=='5':
                print('sent to previous 5')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12345)
    c.close()
