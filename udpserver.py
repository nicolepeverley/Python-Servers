from socket import *
import sys

#create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

#bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
    #wait to receive data
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    #print client data is recieved from
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    
    #send data back
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)

