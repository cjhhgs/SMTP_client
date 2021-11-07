from socket import *
from tkinter.constants import S
from email.base64mime import body_encode
import ssl
import myMail
import base64

def SMTP_send(mail):
    
    mailServer = "smtp.qq.com"
    fromAddress = mail.From
    toAddress = mail.To
    password = mail.Pass
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
    recv1 = sslclientSocket.recv(1024).decode()
    print('1:'+recv1)
    if '250' != recv1[:3]:
        print('250 reply not received from server.')


    #发出登录认证
    loginCommand = 'AUTH login\r\n'
    sslclientSocket.send(loginCommand.encode())
    recv2 = sslclientSocket.recv(1024).decode()
    print('2:'+recv2)

    
    #发送用户名
    fromAddressbass64=base64.b64encode(f'{fromAddress}'.encode())
    userCommand = b'%s\r\n' % fromAddressbass64
    sslclientSocket.send(userCommand)
    recv3 = sslclientSocket.recv(1024).decode()
    print('3:'+recv3)
    #发送授权码
    passwordbase64 =  base64.b64encode(f'{password}'.encode())
    passwordCommand = b'%s\r\n' % passwordbase64
    sslclientSocket.send(passwordCommand)
    recv4 = sslclientSocket.recv(1024).decode()
    print('4:'+recv4)

    
    #发送者的邮箱地址
    mailfromCommand = b'MAIL FROM:<%s>\r\n'%fromAddress.encode()
    sslclientSocket.send(mailfromCommand)
    recv5 = sslclientSocket.recv(1024).decode()
    print('5:'+recv5)


    #收件人邮箱地址
    #可以有多个
    for addr in toAddress:
        mailtoCommand = b'RCPT TO:<%s>\r\n'%addr.encode()
        sslclientSocket.send(mailtoCommand)
        recv6 = sslclientSocket.recv(1024).decode()
        print('6:'+recv6)


    #请求发送邮件信息
    dataCommand = b'DATA\r\n'
    sslclientSocket.send(dataCommand)
    recv7 = sslclientSocket.recv(1024).decode()
    print('7:'+recv7)


    #头部信息
    From = b'From:%s\r\n'%fromAddress.encode()  #发送方
    sslclientSocket.send(From)

    for addr in toAddress:
        To = b'TO:%s\r\n'%addr.encode() #接收方
        sslclientSocket.send(To)

    subject = b'Subject:%s\r\n'%mail.Message.Subject.encode() #主题
    sslclientSocket.send(subject)
    
    sslclientSocket.send(b'\r\n')

    #正文
    sslclientSocket.send(mail.Message.MainText.encode())
    sslclientSocket.send(b'\r\n\r\n.\r\n')

    
    recv8 = sslclientSocket.recv(1024).decode()
    print('8:'+recv8)

    return 0

if __name__ == '__main__':
    # mail = myMail.myMail
    # mail.From = '462072107@qq.com'
    # mail.To = ['462072107@qq.com']
    # mail.Pass = 'wdteskannxwncbcj'

    # message = myMail.mailMessage
    # message.Subject = 'test'
    # message.MainText = 'hello!'

    # mail.Message = message
    
    #SMTP_send(mail)

    main2 = myMail.myMail('462072107@qq.com',
    'wdteskannxwncbcj',
    ['462072107@qq.com'],
    'test2',
    '''
    hello,sjsjjssjsjhhdh
    sdhsjadjjsgdjgsajhgh
    sadhahsjdghasgd
    asgdhasdghg
    ''')
    #SMTP_send(main2)
    print(main2)
    sss={'From':main2.From,'To':main2.To,'Pass':main2.Pass,'Subject':main2.Message.Subject,'Maintext':main2.Message.MainText}
    print(sss)
