from socket import *
from email.base64mime import body_encode
import ssl
import myMail

def SMTP_send(mail):
    
    mailServer = "smtp.qq.com"
    fromAddress = mail.From
    toAddress = mail.To
    userName = "462072107@qq.com"
    password = mail.Pass #"wdteskannxwncbcj"
    serverPort = 587
    clientSocket = socket(AF_INET, SOCK_STREAM)     #建立套接字
    sslclientSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_NONE,ssl_version=ssl.PROTOCOL_SSLv23)    #ssl认证的套接字

    #连接服务器
    sslclientSocket.connect((mailServer, serverPort))   
    recv = sslclientSocket.recv(1024).decode()
    print(recv)
    if '220' != recv[:3]:
        print('220 reply not received from server.')
    
    #发出问候
    heloCommand = 'HELO qq.com\r\n'
    sslclientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if '250' != recv1[:3]:
        print('250 reply not received from server.')


    #发出登录认证
    loginCommand = 'AUTH login\r\n'
    sslclientSocket.send(loginCommand.encode())
    recv2 = sslclientSocket.recv(1024).decode()
    print(recv2)
    #发送用户名
    userCommand = fromAddress+'\r\n'
    sslclientSocket.send(userCommand.encode())
    recv3 = sslclientSocket.recv(1024).decode()
    print(recv3)
    #发送授权码
    passwordCommand = password+'\r\n'
    sslclientSocket.send(passwordCommand.encode())
    recv4 = sslclientSocket.recv(1024).decode()
    print(recv4)

    
    #发送者的邮箱地址
    mailfromCommand = b'MAIL FROM:<%s>\r\n'%fromAddress.encode()
    sslclientSocket.send(mailfromCommand)
    recv5 = sslclientSocket.recv(1024).decode()
    print(recv5)


    #收件人邮箱地址
    #可以有多个
    for addr in toAddress:
        mailtoCommand = b'RCPT TO:<%s>\r\n'%addr.encode()
        sslclientSocket.send(mailtoCommand)
        recv6 = sslclientSocket.recv(1024).decode()
        print(recv6)


    #请求发送邮件信息
    dataCommand = b'DATA\r\n'
    sslclientSocket.send(dataCommand)
    recv7 = sslclientSocket.recv(1024).decode()
    print(recv7)


    #头部信息
    From = b'From:%s\r\n'%fromAddress.encode()  #发送方
    sslclientSocket.send(From)

    for addr in toAddress:
        To = b'TO:%s\r\n'%addr.encode() #接收方
        sslclientSocket.send(To)

    subject = b'Subject:%s\r\n'%mail.mailMessage.Subject.encode() #主题
    sslclientSocket.send(subject)
    
    sslclientSocket.send(b'\r\n')

    #正文
    sslclientSocket.send(mail.mailMessage.MainText.encode())
    sslclientSocket.send(b'\r\n.\r\n')

    
    recv8 = clientSocket.recv(1024).decode()
    print(recv8)

    return 0

if __name__ == '__main__':
    mail = myMail
    mail.From = '462072107@qq.com'
    mail.To = '462072107@qq.com'
    mail.Pass = 'wdteskannxwncbcj'
    
    SMTP_send("Hello","462072107@qq.com")