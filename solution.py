from socket import *


def smtp_client(port=25, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))


    # Fill in end

    recv = clientSocket.recv(1024).decode()
   # print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELLO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
   # print(recv1)
   # if recv1[:3] != '250':
      #  print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = 'MAIL FROM: <mail@mail.com>\r\n.'
    clientSocket.send(mailfromCommand)
    recv1 = clientSocket.recv(1024)
   # print(recv1)
   # if recv1[:3] != '250':
       # print('mail from 250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcpttoCommand = 'RCPT TO: <aa8701@nyu.edu>\r\n'
    clientSocket.send(rcpttoCommand)
    recv1 = clientSocket.recv(1024)
       #print(recv1)
   # if recv1[:3] != '250':
          # print('rcpt to 250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'Data'
          #print(dataCommand)
    clientSocket.send(dataCommand)
    recv1 = clientSocket.recv(1024)
          #print(recv1)
    #if recv1[:3] != '250':
              #print('data 250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    message = raw_input('Enter Message Here: ')
    # Fill in end

    # Message ends with a single period.
    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message + mailMessageEnd)
    recv1 = clientSocket.recv(1024)
    #print(recv1)
   # if recv1[:3] != '250':
        #print('end msg 250 reply not received from server.')

    # Fill in start

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'Quit\r\n'
    #    print(quitCommand)
    clientSocket.send(quitCommand)
    recv1 = clientSocket.recv(1024)
    #    print(recv1)
    if recv1[:3] != '250':
    #        print('quit 250 reply not received from server.')
        pass
    # Fill in end


if __name__ == '__main__':
    smtp_client(25, '127.0.0.1')
