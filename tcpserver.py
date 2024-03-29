import socket
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listen for incoming connections
sock.listen(1)

while True:
    #wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        #print client that is connected
        print >>sys.stderr, 'connection from', client_address

        #receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        #close the connection
        connection.close()
