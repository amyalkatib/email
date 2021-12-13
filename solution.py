from socket import *


def smtp_client(port=1025, mailserver= '127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #mailserver = 'nyu.edu'
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket()
    clientSocket.connect((mailserver, port))
    #clientSocket.listen()
    #conn,addr = clientSocket.accept()
    #clientSocket.connect((mailserver, port))
    #print('omg fml')
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
   # print(recv)
   # if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    HELOCommand = 'HELO Alice\r\n'
    clientSocket.send(HELOCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
   # print(recv1)
    #if recv1[:3] != '250':
       # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    MAILFROMCommand = "MAIL FROM:<aa8701@nyu.edu>\r\n"
    clientSocket.send(MAILFROMCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(rec2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    RCPTTOCommand = "RCPT TO:<aa8701@nyu.com>\r\n"
    clientSocket.send(RCPTTOCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
       # print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    DATACommand = "DATA\r\n"
    clientSocket.send(DATACommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    #recv_msg = clientSocket.recv(1024).decode()
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    QUITCommand = "QUIT\r\n"
    clientSocket.send(QUITCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    clinetSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
