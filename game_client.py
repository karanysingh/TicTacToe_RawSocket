import socket,time
s = socket.socket()
HOST = '127.0.0.1'
s.connect((HOST,9090))
while True:
    print(s.recv(1024).decode())
    vals = input(":")
    if(len(vals.split())==2):
        s.send(vals.encode())
    else:
        print("invalid input")
        endd = input('Do you want to end?(y/n)')
        if(endd=='y'):
            break
        elif(endd=='n'):
            pass

s.close()
