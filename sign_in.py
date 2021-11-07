import tkinter as tk

from tkinter import ttk
import tkinter
'''先写个登录框框吧，直接上函数吧，类真的累'''
def login(master):
 
    login_frame = tk.Frame(master)
    login_frame.grid(padx=300,pady=180)
 
    ttk.Label(login_frame,text='用户名').grid(column=1,row=1,columnspan=2)
    ttk.Entry(login_frame,).grid(column=3,row=1,columnspan=3)
 
    ttk.Label(login_frame,text='密码').grid(column=1,row=2,columnspan=2)
    ttk.Entry(login_frame,).grid(column=3,row=2,columnspan=3)
 
    def reg():
        '''这里就写你的登录需要的内容就行'''
        reg_top=tk.Toplevel(login_frame)
        tk.Label(reg_top,text='用户注册').grid(column=2,row=2)
 
    def cert():
        '''这里需要验证用户名和密码对不对，不对就蹦出个对话框告诉他，对就destroy'''
        login_frame.destroy()#我这里为了测试直接销毁了
 
    #ttk.Button(login_frame,text='注册',command=reg).grid(column=2,row=3,columnspan=2,pady=15)
    ttk.Button(login_frame,text='登录',command=cert).grid(column=3,row=3,pady=15)
 
    return login_frame  # 这里一定要return啊

'''下面就是用户登录成功了应该出现的页面'''
def index():
    master = tk.Tk()
    index_frame =tk.Frame(master)
    index_frame.grid()
    text=tk.Text(index_frame)
    text.grid()
    text.insert('end','没错你登录成功，所以看到了我')

def handler_sign_in(window):
    main_window(window)

def main_window(window):
    window.geometry('600x400')
    window.title("mail box")
    window.mainloop()

def sign_in(window):  #包装登录界面
    
    window.title("sign in")
    window.geometry("300x180")

    # 标签位置还需调
    ttk.Label(window,text='用户名').grid(column=2,row=3,columnspan=2)
    ttk.Entry(window,).grid(column=4,row=3,columnspan=3)
 
    ttk.Label(window,text='密码').grid(column=1,row=5,columnspan=2)
    ttk.Entry(window,).grid(column=3,row=5,columnspan=3)

    btn2=ttk.Button(window,text='登录',command=lambda: handler_sign_in(window))
    btn2.place(relx=0.3, rely=0.4, relwidth=0.3, relheight=0.2)
    
    window.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    sign_in(window)