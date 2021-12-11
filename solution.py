from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    HELOCommand = 'HELO Alice\r\n'
    clientSocket.send(HELOCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    MAILFROMCommand = "MAIL FROM:<aa8701@nyu.edu>\r\n"
    clientSocket.send(MAILFROMCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in start
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    RCPTTOCommand = "RCPT TO:<aa8701@nyu.com>\r\n"
    clientSocket.send(RCPTTOCommand.encode())
r   ecv3 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    DATACommand = "DATA\r\n"
    clientSocket.send(DATACOmmand.encode())
    recv4 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    recv_msg = clientSocket.recv(1024).decode()
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv_endmsg = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    QUITCommand = "QUIT\r\n"
    clientSocket.send(QUITCommand.encode())
    recv5 = clientSocket.recv(1024).decode()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
