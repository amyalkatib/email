from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"



# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverport))
recv = clientSocket.recv(1024)
print (recv)
#if recv[:3] != '220':
    #print ('220 reply not received from server.')
# Send HELO command and print server response.
print ("Sending First HELO")
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print (recv1)
#if recv1[:3] != '250':
    #print ('250 reply not received from server.')
# Send MAIL FROM command and print server response.
print ("Sending MAIL FROM Command")
mailFromCommand = bytes("MAIL FROM: <aa8701@nyu.edu>\r\n", "utf-8")
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print (recv1)
#if recv1[:3] != '250':
    #print ('250 reply not received from server')
# Send RCPT TO command and print server response.
print ("Sending RCPT TO Command")
rcptToCommand = bytes("RCPT TO: <aa8701@nyu.edu>\r\n", "utf-8")
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024)
print (recv1)
#if recv1[:3] != '250':
   # print ('250 reply not received from server')
# Send DATA command and print server response.

# Send DATA command and print server response
dataCommand = 'Data'
#print(dataCommand)
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
#print(recv1)
#if recv1[:3] != '250':
    #print('data 250 reply not received from server.')

# Send message data.
message = raw_input('Enter Message Here: ')

# Fill in end# Message ends with a single period.
mailMessageEnd = '\r\n.\r\n'
clientSocket.send(message + mailMessageEnd)
recv1 = clientSocket.recv(1024)
#print(recv1)
#if recv1[:3] != '250':
    #print('end msg 250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
#print(quitCommand)
clientSocket.send(quitCommand)
recv1 = clientSocket.recv(1024)
#print(recv1)
#if recv1[:3] != '250':
    #print('quit 250 reply not received from server.')

    #pass

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
