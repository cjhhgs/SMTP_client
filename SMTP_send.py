from socket import *
from tkinter.constants import S
from email.base64mime import body_encode
import ssl
import myMail
import base64


##错误码表
# 1：连接失败
# 2：用户名错误
# 3：密码错误
# 4: 收件人信息错误
# 5：邮件信息格式错误
def SMTP_send(mail):
    
    mailServer = "smtp.qq.com"
    fromAddress = mail.From
    password = mail.Pass
    user = mail.User
    toAddress = mail.To
    
    serverPort = 587
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)     #建立套接字
        sslclientSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_NONE,ssl_version=ssl.PROTOCOL_SSLv23)    #ssl认证的套接字
    except:
        return 1
    else:
        print("套接字连接成功")

    #连接服务器
    try:
        sslclientSocket.connect((mailServer, serverPort))   
    except:
        return 1
    recv = sslclientSocket.recv(1024).decode()
    print(recv)
    if '220' != recv[:3]:
        print('220 reply not received from server.')
        return 1
    
    #发出问候
    heloCommand = 'HELO qq.com\r\n'
    sslclientSocket.send(heloCommand.encode())
    recv1 = sslclientSocket.recv(1024).decode()
    print('1:'+recv1)
    if '250' != recv1[:3]:
        print('250 reply not received from server.')
        return 1


    #发出登录认证
    loginCommand = 'AUTH login\r\n'
    sslclientSocket.send(loginCommand.encode())
    recv2 = sslclientSocket.recv(1024).decode()
    print('2:'+recv2)
    if '334'!=recv2[:3]:
        print('334 reply not received from server.')
        return 1

    
    #发送用户名
    fromAddressbass64=base64.b64encode(f'{fromAddress}'.encode())
    userCommand = b'%s\r\n' % fromAddressbass64
    sslclientSocket.send(userCommand)
    recv3 = sslclientSocket.recv(1024).decode()
    print('3:'+recv3)
    if '334' != recv3[:3]:
        print('334 reply not received from server.')
        return 2


    #发送授权码
    passwordbase64 =  base64.b64encode(f'{password}'.encode())
    passwordCommand = b'%s\r\n' % passwordbase64
    sslclientSocket.send(passwordCommand)
    recv4 = sslclientSocket.recv(1024).decode()
    print('4:'+recv4)
    if '235' != recv4[:3]:
        print('235 reply not received from server.')
        return 3

    
    #发送者的邮箱地址
    mailfromCommand = b'MAIL FROM:<%s>\r\n'%fromAddress.encode()
    sslclientSocket.send(mailfromCommand)
    recv5 = sslclientSocket.recv(1024).decode()
    print('5:'+recv5)
    if '250' != recv5[:3]:
        print('250 reply not received from server.')
        return 2


    #收件人邮箱地址
    #可以有多个
    for addr in toAddress:
        mailtoCommand = b'RCPT TO:<%s>\r\n'%addr.encode()
        sslclientSocket.send(mailtoCommand)
        recv6 = sslclientSocket.recv(1024).decode()
        print('6:'+recv6)
        if '250' != recv6[:3]:
            print('250 reply not received from server.')
            return 4


    #请求发送邮件
    dataCommand = b'DATA\r\n'
    sslclientSocket.send(dataCommand)
    recv7 = sslclientSocket.recv(1024).decode()
    print('7:'+recv7)
    if '354' != recv7[:3]:
        print('354 reply not received from server.')
        return 1


    #头部信息
    From = b'From:%s\r\n'%user.encode()  #发送方
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
    if '250' != recv8[:3]:
        print('250 reply not received from server.')
        return 5

    quitcommand = 'QUIT\r\n'
    sslclientSocket.send(quitcommand.encode())
    recv9 = sslclientSocket.recv(1024).decode()
    print('9:'+recv9)
    if('221' != recv9[:3]):
        print('221 reply not received from server.')
        return 1

    return 0


# 错误码表
# 1： 连接错误
# 2： 用户名错误
# 3： 密码错误
def login(user,password):
    mailServer = "smtp.qq.com"
    serverPort = 587
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)     #建立套接字
        sslclientSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_NONE,ssl_version=ssl.PROTOCOL_SSLv23)    #ssl认证的套接字
    except:
        return 1

    #连接服务器
    try:
        sslclientSocket.connect((mailServer, serverPort)) 
    except:
        return 1  
    recv = sslclientSocket.recv(1024).decode()
    print(recv)
    if '220' != recv[:3]:
        print('220 reply not received from server.')
        return 1
    
    #发出问候
    heloCommand = 'HELO qq.com\r\n'
    sslclientSocket.send(heloCommand.encode())
    recv1 = sslclientSocket.recv(1024).decode()
    print('1:'+recv1)
    if '250' != recv1[:3]:
        print('250 reply not received from server.')
        return 1


    #发出登录认证
    loginCommand = 'AUTH login\r\n'
    sslclientSocket.send(loginCommand.encode())
    recv2 = sslclientSocket.recv(1024).decode()
    print('2:'+recv2)
    if ('334' != recv2[:3]):
        print('334 reply not received from server.')
        return 1

    
    #发送用户名
    fromAddressbass64=base64.b64encode(f'{user}'.encode())
    userCommand = b'%s\r\n' % fromAddressbass64
    sslclientSocket.send(userCommand)
    recv3 = sslclientSocket.recv(1024).decode()
    print('3:'+recv3)
    if ('334' != recv3[:3]):
        print('334 reply not received from server.')
        return 2

    #发送授权码
    passwordbase64 =  base64.b64encode(f'{password}'.encode())
    passwordCommand = b'%s\r\n' % passwordbase64
    sslclientSocket.send(passwordCommand)
    recv4 = sslclientSocket.recv(1024).decode()
    print('4:'+recv4)
    if ('235' != recv4[:3]):
        print('235 reply not received from server.')
        return 3

    quitcommand = 'QUIT\r\n'
    sslclientSocket.send(quitcommand.encode())
    recv5 = sslclientSocket.recv(1024).decode()
    print('5:'+recv5)
    if('221' != recv5[:3]):
        print('221 reply not received from server.')
        return 1

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

    # main2 = myMail.myMail('462072107@qq.com',
    # 'wdteskannxwncbcj',
    # '462072107',
    # ['462072107@qq.com'],
    # 'test2',
    # '''
    # hello,sjsjjssjsjhhdh
    # sdhsjadjjsgdjgsajhgh
    # sadhahsjdghasgd
    # asgdhasdghg
    # ''')
    # SMTP_send(main2)

    login('462072107@qq.com','wdteskannxwncbcj')
