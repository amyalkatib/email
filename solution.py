from socket import *
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    heloCommand = bytes("HELO Alice\r\n", "utf-8")
# Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = "127.0.0.1"
    serverport = 1025
# Create socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, serverport))
    recv = clientSocket.recv(1024)
    #print (recv)
    #if recv[:3] != '220':
        #print ('220 reply not received from server.')
# Send HELO command and print server response.
    print ("Sending First HELO")
    clientSocket.send(heloCommand)
    recv1 = clientSocket.recv(1024)
    #print (recv1)
    #if recv1[:3] != '250':
        #print ('250 reply not received from server.')
# Send MAIL FROM command and print server response.
    #print ("Sending MAIL FROM Command")
    mailFromCommand = bytes("MAIL FROM: <aa8701@nyu.edu>\r\n", "utf-8")
    clientSocket.send(mailFromCommand)
    recv1 = clientSocket.recv(1024)
    #print (recv1)
   # if recv1[:3] != '250':
     #   print ('250 reply not received from server')
# Send RCPT TO command and print server response.
   # print ("Sending RCPT TO Command")
    rcptToCommand = bytes("RCPT TO: <aa8701@nyu.edu>\r\n", "utf-8")
    clientSocket.send(rcptToCommand)
    recv1 = clientSocket.recv(1024)
   # print (recv1)
    #if recv1[:3] != '250':
       # print ('250 reply not received from server')
# Send DATA command and print server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    #print("After DATA command: "+recv4)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

# Send message data.
    subject = "Subject: SMTP mail client testing \r\n\r\n" 
    clientSocket.send(subject.encode())
    message = raw_input("Enter your message: \r\n")
    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    #print("Response after sending message body:"+recv_msg.decode())
    #if recv1[:3] != '250':
    #print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024)
#print (message)
clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
