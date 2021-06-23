import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
recv_addr=("3.235.20.173",9999)
while 2 > 1 :
    user_data=input("enter your message :- ")
    newdata=user_data.encode('ascii')
    s.sendto(newdata,recv_addr)
    time.sleep(2)
    print("your message has been sent...")