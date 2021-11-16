
import tkinter
from tkinter import font
import tkinter.messagebox
from tkinter import ttk
from tkinter.constants import BOTH, S, X,Y, BOTTOM, LEFT, TOP, TRUE
import SMTP_send
import myMail
import os
import ast
import datetime

class mail_GUI():
    window = tkinter.Tk()
    var_usr_name = tkinter.StringVar()
    var_usr_pwd = tkinter.StringVar()
    var_user = tkinter.StringVar()
    var_recive = tkinter.StringVar()
    var_subject = tkinter.StringVar()
    var_text = tkinter.StringVar()
    var_save_name = tkinter.StringVar()
    user=''
    password=''

    def __init__(self):
        self.window.title("e-mail")
        self.window.geometry('800x600')
        self.frame = tkinter.Frame(self.window,bg='white')
        self.frame.pack(expand=TRUE,fill=BOTH)
        
        l = tkinter.Label(self.frame, text='Hello！this is my e-mail',bg='white',font=('Arial', 12), width=30, height=2)
        l.place(x=250,y=170)

        btn1=tkinter.Button(self.frame,text='进入',font=('Arial', 12),bg='white', width=10, height=1,command=self.sign_in)
        btn1.place(x=350,y=250)

        self.window.mainloop()

    #登录界面
    def sign_in(self):
        self.frame.destroy()
        self.frame2 = tkinter.Frame(self.window, relief='sunken',bg='white')
        self.frame2.pack(expand=TRUE,fill=BOTH)
        self.frame2.lift()
        
        #标签栏
        l1 =tkinter.Label(self.frame2, text='User name:', font=('Arial', 14))
        l1.place(x=200,y=170)

        l1=tkinter.Label(self.frame2, text=' Password :', font=('Arial', 14))
        l1.place(x=200,y=210)

        # 第6步，用户登录输入框entry
        # 用户名
        self.var_usr_name.set('462072107@qq.com')
        entry_usr_name = tkinter.Entry(self.frame2, textvariable=self.var_usr_name, font=('Arial', 14))
        entry_usr_name.place(x=310,y=175)

        # 用户密码
        self.var_usr_pwd.set('wdteskannxwncbcj')
        entry_usr_pwd = tkinter.Entry(self.frame2, textvariable=self.var_usr_pwd, font=('Arial', 14))
        entry_usr_pwd.place(x=310,y=215)

        
        btn_login = tkinter.Button(self.frame2, text='登录',font=('Arial', 12), width=10, height=1,command=self.handler_sign_in)
        btn_login.place(x=370, y=250)


    def handler_sign_in(self):
        self.user = self.var_usr_name.get()
        self.password = self.var_usr_pwd.get()

        print("开始验证")
        code = SMTP_send.login(self.user,self.password)
        if(code==0):
            print("right")
            self.main_view()
        elif(code==1):
            print("wroung")
            tkinter.messagebox.showerror('错误','连接失败，请重试')
        elif(code==2):
            tkinter.messagebox.showerror('错误','用户名不存在')
        elif(code==3):
            tkinter.messagebox.showerror('错误','授权码错误')

    def main_view(self):
        print("log in")
        self.frame2.destroy()

        self.frame3 = tkinter.Frame(self.window, relief='sunken',bg='white')
        self.frame3.pack(expand=TRUE,fill=BOTH)
        self.frame3.lift()

        #frame4 ： 左侧框架
        self.frame4 = tkinter.Frame(self.frame3,relief='sunken',height=600 ,width=200,bd=3 ,bg='white')
        self.frame4.place(x=0,y=0)
        #self.frame4.lift()

        #frame5 : 右侧框架
        self.frame5 = tkinter.Frame(self.frame3,relief='sunken',height=600 ,width=600,bd=3 )
        self.frame5.place(x=200,y=0)
        self.frame5.lift()

        btn1 = tkinter.Button(self.frame4, text='新建',font=('Arial', 12), width=20, height=2,command=self.handler_new)
        btn1.place(x=0,y=0)
        btn2 = tkinter.Button(self.frame4, text='保存',font=('Arial', 12), width=20, height=2,command=self.handler_save)
        btn2.place(x=0,y=60)
        btn3 = tkinter.Button(self.frame4, text='草稿箱',font=('Arial', 12), width=20, height=2,command=self.handler_mailbox)
        btn3.place(x=0,y=120)
        btn4 = tkinter.Button(self.frame4,text='发送',font=('Arial', 12) ,width=20, height=2,command=self.handler_send_mail)
        btn4.place(x=0,y=180)
        btn5 = tkinter.Button(self.frame4,text='已发送',font=('Arial', 12) ,width=20, height=2,command=self.handler_sended)
        btn5.place(x=0,y=240)

        
        
        lable1 = tkinter.Label(self.frame5,text='发件人：',font=('Arial', 12))
        lable1.place(x=1,y=10,width=100,height=30)
        self.var_user.set(self.user)
        entry_user = tkinter.Entry(self.frame5, textvariable=self.var_user, font=('Arial', 12))
        entry_user.place(x=100,y=10,width=450, height=30)

        lable2 = tkinter.Label(self.frame5,text='收件人：',font=('Arial', 12))
        lable2.place(x=1,y=50,width=100,height=30)
        entry_recive = tkinter.Entry(self.frame5, textvariable=self.var_recive, font=('Arial', 12))
        entry_recive.place(x=100,y=50,width=450, height=30)

        btn_addrs = tkinter.Button(self.frame5,text='+',font=('Arial', 12) ,width=2, height=1,command=self.handler_addrs)
        btn_addrs.place(x=560,y=50)

        lable3 = tkinter.Label(self.frame5,text=' 主题：',font=('Arial', 12))
        lable3.place(x=1,y=90,width=100,height=30)
        entry_subject = tkinter.Entry(self.frame5, textvariable=self.var_subject, font=('Arial', 12))
        entry_subject.place(x=100,y=90,width=450, height=30)

        lable4 = tkinter.Label(self.frame5,text='正文：',font=('Arial', 12))
        lable4.place(x=1,y=130,width=100,height=30)
        self.entry_text = tkinter.Text(self.frame5,  font=('Arial', 12),width=46, height=20)
        self.entry_text.place(x=100,y=130)
        self.entry_text.insert(1.0, self.var_text.get())

       

    def handler_new(self):
        self.var_recive.set('')
        self.var_subject.set('')
        self.entry_text.delete(1.0,"end")

        print(1)
    # 保存到草稿箱的处理函数
    def handler_save(self):
        print("save")
        window_save = tkinter.Toplevel(self.window)
        window_save.geometry('300x100')
        window_save.title('save to box')

        
        self.var_save_name.set('待发送邮件')
        tkinter.Label(window_save,text='保存邮件名：').place(x=10,y=20)
        entry_save_name = tkinter.Entry(window_save,textvariable=self.var_save_name)
        entry_save_name.place(x=130,y=20)

        btn_comfirm_save = tkinter.Button(window_save,text='保存',command=self.save)
        btn_comfirm_save.place(x=150,y=60)

    def save(self):
        
        new_name = self.var_save_name.get()+'.txt'

        #检查是否文件重名
        filepath=os.getcwd()+'\save_box'
        files = os.listdir(filepath)
        print(files)

        for file in files:
            if(file==new_name):
                tkinter.messagebox.showerror('错误','文件名已存在')
                return 1

        
        Username = self.var_user.get()
        Receive = self.var_recive.get()
        Subject=self.var_subject.get()
        Text=self.entry_text.get(1.0,"end")

        save_file = {'Username':Username,'Receive':Receive,'Subject':Subject,'Text':Text}

        full_path = filepath + '\\'+new_name
        new_file = open(full_path, 'w')
        
        new_file.write(str(save_file))
        new_file.close()

        tkinter.messagebox.showinfo('提示','保存成功')

    #通讯录处理函数
    def handler_addrs(self):
        self.recieve_list = []  #获取文件中的通讯录信息
        f = open('addrs.txt',"r")
        s = f.read()
        f.close()
        self.recieve_list = s.split(';')
        
        window_addrs = tkinter.Toplevel(self.window)
        window_addrs.geometry('300x100')
        window_addrs.title('select receive addresss')

        tkinter.Button(window_addrs,text='新建',command=self.handler_new_addrs).place(x=60,y=60)
        self.var_new_receive=tkinter.Variable()
        tkinter.Entry(window_addrs,textvariable=self.var_new_receive, font=('Arial', 12)).place(x=100,y=60,width=180, height=20)
        

        tkinter.Label(window_addrs,text='收件人：').place(x=10,y=20)
        self.comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
        self.comvalue.set("选择收件人")
        self.comboxlist=ttk.Combobox(window_addrs,textvariable=self.comvalue)
        self.comboxlist["values"]=tuple(self.recieve_list)
        #self.comboxlist.current(0) #选择第一个
        self.comboxlist.bind("<<ComboboxSelected>>",self.select_addr) #绑定事件,(下拉列表框被选中时，绑定go()函数)
        self.comboxlist.place(x=100,y=20)

    def select_addr(self,event):
        s = self.comboxlist.get()   #新选的
        print(s)
        x = self.var_recive.get()   #已有的
        recive_list = x.split(';')

        for i in recive_list:
            if(i==s):
                s=''
        if(s!='' and x!=''):
            y = x+';'+s
        elif(s!='' and x==''):
            y=s
        else:
            y=x

        print(y)
        self.var_recive.set(y)

    def handler_new_addrs(self):
        ff = open('addrs.txt','r')
        ss = ff.read()
        ff.close()
        print(ss)
        s = self.var_new_receive.get()
        self.var_new_receive.set('')
        if(s!=''):
            f = open('addrs.txt','a')
            if(ss==''):
                f.write(s)
            else:
                f.write(';'+s)
            f.close()

            f = open('addrs.txt',"r")
            s = f.read()
            f.close()
            self.recieve_list = s.split(';')
            self.comboxlist["values"]=tuple(self.recieve_list)
    

    def handler_mailbox(self):

        window_mailbox = tkinter.Toplevel(self.window)
        window_mailbox.geometry('300x100')
        window_mailbox.title('select from mailbox')

        
        filepath=os.getcwd()+'\save_box'
        files = os.listdir(filepath)
        self.mail_list=files   #提取邮件列表

        tkinter.Label(window_mailbox,text='选择邮件：').place(x=10,y=20)
        self.var_select_mail=tkinter.StringVar()#窗体自带的文本，新建一个值
        self.var_select_mail.set("")
        self.comboxlist=ttk.Combobox(window_mailbox,textvariable=self.var_select_mail)
        self.comboxlist["values"]=tuple(self.mail_list)
        #self.comboxlist.current(0) #选择第一个
        #self.comboxlist.bind("<<ComboboxSelected>>") #绑定事件,(下拉列表框被选中时，绑定go()函数)
        self.comboxlist.place(x=100,y=20)

        tkinter.Button(window_mailbox,text='确定',command=self.handler_select_mail).place(x=120,y=60)
        
       
    def handler_select_mail(self):
        file = self.var_select_mail.get()
        filepath=os.getcwd()+'\save_box\\'+file
        f = open(filepath,'r')
        context = f.read()
        print(context)
        dict = ast.literal_eval(context)

        self.var_user.set( dict["Username"])
        self.var_recive.set(dict["Receive"])
        self.var_subject.set(dict["Subject"])
        self.var_text.set(dict["Text"])
        self.entry_text.delete(1.0, "end")
        self.entry_text.insert(1.0, dict["Text"])
        
        print(1)

    def handler_send_mail(self):
        useraddr = self.var_usr_name.get()
        password = self.var_usr_pwd.get()

        username = self.var_user.get()
        receive = self.var_recive.get().split(';')

        subject = self.var_subject.get()
        text = self.entry_text.get(1.0,"end")
        print(useraddr,password,username,receive,subject,text)
        main2 = myMail.myMail(useraddr,password,username,receive,subject,text)
        
        code = SMTP_send.SMTP_send(main2)
        if code == 0:
            tkinter.messagebox.showinfo('提示','发送成功')
            self.save_to_sended()
            print("success")
        elif code == 1:
            tkinter.messagebox.showerror('错误',"连接错误，请重试")
        elif code == 4:
            tkinter.messagebox.showerror('错误',"收件人信息错误")
        elif code == 5:
            tkinter.messagebox.showerror('错误',"邮件格式错误")


    def save_to_sended(self):
        curr_time = datetime.datetime.now()# 2019-07-06 14:55:56.873893 <class 'datetime.datetime'>
        time_str = datetime.datetime.strftime(curr_time,'%Y%m%d%H%M%S')# 2019-07-06 15:50:12
        
        Username = self.var_user.get()
        Receive = self.var_recive.get()
        Subject=self.var_subject.get()
        Text=self.entry_text.get(1.0,"end")

        save_file = {'Username':Username,'Receive':Receive,'Subject':Subject,'Text':Text}

        #检查是否文件重名
        filepath=os.getcwd()+'\sended_box'
        full_path = filepath + '\\'+time_str+'--\''+Subject+'\''
        print(full_path)
        new_file = open(full_path, 'w')
        print(2)
        
        new_file.write(str(save_file))
        new_file.close()
        print(1)


    def handler_sended(self):
        window_sended = tkinter.Toplevel(self.window)
        window_sended.geometry('400x300')
        window_sended.title('sended mail')

        tkinter.Label(window_sended,text='已发送邮件',font=('Arial', 12)).place(x=10,y=10)

        var = tkinter.StringVar()
        
        #创建Listbox
        self.lb = tkinter.Listbox(window_sended, listvariable=var,font=('Arial', 12),width=40)  #将var2的值赋给Listbox
        self.lb.place(x=10,y=50)

        #打开文件
        filepath=os.getcwd()+'\sended_box'
        files = os.listdir(filepath)
        self.sended_list=files   #提取邮件列表
        var.set(tuple(self.sended_list))

        tkinter.Button(window_sended,text='打开',command=self.handler_open_sended).place(x=10,y=250)
        
        print(1)

    def handler_open_sended(self):
        file = self.lb.get(self.lb.curselection())
        filepath=os.getcwd()+'\sended_box\\'+file
        f = open(filepath,'r')
        context = f.read()
        print(context)
        dict = ast.literal_eval(context)

        self.var_user.set( dict["Username"])
        self.var_recive.set(dict["Receive"])
        self.var_subject.set(dict["Subject"])
        self.var_text.set(dict["Text"])
        self.entry_text.delete(1.0, "end")
        self.entry_text.insert(1.0, dict["Text"])
        print(1)

    def new_mail():
        print(1)



if __name__ == '__main__':
    win=mail_GUI()
   

# pyinstaller -F test.py -w
