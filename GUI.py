
import tkinter
from tkinter.constants import BOTH, X,Y, BOTTOM, LEFT, TOP, TRUE
import SMTP_send

class mail_GUI():
    window = tkinter.Tk()
    var_usr_name = tkinter.StringVar()
    var_usr_pwd = tkinter.StringVar()
    var_user = tkinter.StringVar()
    var_recive = tkinter.StringVar()
    var_subject = tkinter.StringVar()
    var_text = tkinter.StringVar()


    def __init__(self):
        self.window.title("e-mail")
        self.window.geometry('800x600')
        self.frame = tkinter.Frame(self.window,bg='white')
        self.frame.pack(expand=TRUE,fill=BOTH)
        
        l = tkinter.Label(self.frame, text='你好！this is my e-mail', bg='red',font=('Arial', 12), width=30, height=2)
        l.pack()

        btn1=tkinter.Button(self.frame,text='进入',bg='red',font=('Arial', 12), width=10, height=1,command=self.sign_in)
        btn1.pack()

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
        self.var_usr_name.set('example@qq.com')
        entry_usr_name = tkinter.Entry(self.frame2, textvariable=self.var_usr_name, font=('Arial', 14))
        entry_usr_name.place(x=310,y=175)

        # 用户密码
        entry_usr_pwd = tkinter.Entry(self.frame2, textvariable=self.var_usr_pwd, font=('Arial', 14))
        entry_usr_pwd.place(x=310,y=215)

        
        btn_login = tkinter.Button(self.frame2, text='登录',font=('Arial', 12), width=10, height=1,command=self.handler_sign_in)
        btn_login.place(x=370, y=250)


    def handler_sign_in(self):
        self.user = self.var_usr_name.get()
        self.password = self.var_usr_pwd.get()

        print("开始验证")
        if_right = SMTP_send.login(self.user,self.password)
        if(if_right==1):
            print("right")
            self.main_view()
        else:
            print("wroung")

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

        btn1 = tkinter.Button(self.frame4, text='新建',font=('Arial', 12), width=20, height=2)
        btn1.place(x=0,y=0)
        btn2 = tkinter.Button(self.frame4, text='保存',font=('Arial', 12), width=20, height=2)
        btn2.place(x=0,y=60)
        btn3 = tkinter.Button(self.frame4, text='草稿箱',font=('Arial', 12), width=20, height=2)
        btn3.place(x=0,y=120)

        
        
        lable1 = tkinter.Label(self.frame5,text='发件人：',font=('Arial', 12))
        lable1.place(x=1,y=10,width=100,height=30)
        entry_user = tkinter.Entry(self.frame5, textvariable=self.var_user, font=('Arial', 12))
        entry_user.place(x=100,y=10,width=450, height=30)

        lable2 = tkinter.Label(self.frame5,text='收件人：',font=('Arial', 12))
        lable2.place(x=1,y=50,width=100,height=30)
        entry_recive = tkinter.Entry(self.frame5, textvariable=self.var_recive, font=('Arial', 12))
        entry_recive.place(x=100,y=50,width=450, height=30)

        lable3 = tkinter.Label(self.frame5,text=' 主题：',font=('Arial', 12))
        lable3.place(x=1,y=90,width=100,height=30)
        entry_subject = tkinter.Entry(self.frame5, textvariable=self.var_subject, font=('Arial', 12))
        entry_subject.place(x=100,y=90,width=450, height=30)

        lable4 = tkinter.Label(self.frame5,text='正文：',font=('Arial', 12))
        lable4.place(x=1,y=130,width=100,height=30)
        entry_text = tkinter.Text(self.frame5,  font=('Arial', 12),width=46, height=20)
        entry_text.place(x=100,y=130)
        entry_text.insert(1.0, self.var_text.get())

        btn_send = tkinter.Button(self.frame5,text='发送',font=('Arial', 12) ,width=10, height=1)
        btn_send.place(x=100,y=500)
        btn_save = tkinter.Button(self.frame5,text='保存',font=('Arial', 12) ,width=10, height=1)
        btn_save.place(x=200,y=500)

        
        


    def new_mail():
        print(1)



if __name__ == '__main__':
    win=mail_GUI()
   
