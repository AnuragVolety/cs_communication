#### server program for B

import socket               
import client_A
import json
# next create a socket object
s = socket.socket()         
print "Socket successfully created"
port = 12341          
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
        if len(path_list)>1 and '1' in path_list:
            print('Packet discarded ', path_list,data)
        elif data['receiver']!="1":
            if data['sender']!='1':
                data['path']+=' 1'
            i_msg = json.dumps(data)
            client_A.send(i_msg,12342) 
            client_A.send(i_msg,12345)
        else:
            path_list = [str(x) for x in data['path'].split()]
            print('Path found', path_list)   
            data['pathFound']='1'
            data['path']+=' 1'
            i_msg = json.dumps(data)
            if path_list[-1]=='2':
                client_A.send(i_msg,12342)
            elif path_list[-1]=='5':
                client_A.send(i_msg,12345)
            #print('sender '+data['sender'] +' receiver '+data['receiver'] + ' data : '+data['data'])
    else:
        if data['sender']=='1':
            print(' Received the poling packet')
            print(data['path'])
        else:
            path_list = [str(x) for x in data['path'].split()]
            pos = path_list.index('1')
            if path_list[pos-1]=='2':
                print('sent to previous 2')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12342)
            elif path_list[pos-1]=='5':
                print('sent to previous 5')
                print(path_list[0:pos-1],'cut')
                client_A.send(d,12345)

    c.close()
