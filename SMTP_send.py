from socket import *
from email.base64mime import body_encode

def SMTP_send(message,toAddressList):
    message = message + "\r\n"
    mailServer = "smtp.qq.com"
    fromAddress = "462072107@qq.com"
    userName = "462072107@qq.com"
    password = "wdteskannxwncbcj"
    serverPort = 587
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailServer, serverPort))

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if '220' != recv[:3]:
        print('220 reply not received from server.')
    
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if '250' != recv1[:3]:
        print('250 reply not received from server.')


    user_pass_encode64 = body_encode(f"\0{userName}\0{password}".encode('ascii'), eol='')
    clientSocket.sendall(f'AUTH PLAIN {user_pass_encode64}\r\n'.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)

    return 0

if __name__ == '__main__':
    SMTP_send("Hello","462072107@qq.com")