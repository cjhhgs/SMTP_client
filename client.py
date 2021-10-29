import SMTP_send
import myMail
from tkinter import *

class myClient():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
    

def send():

    return 0

def GUI():
    window = Tk()
    window.title('mymail')
    window.geometry('320x160+10+10')#290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
    window.geometry('1068x681+10+10')

    init_data_label = Label(window, text="待处理数据")
    init_data_label.grid(row=0, column=0)
    init_data_Text = Text(window, width=100, height=160)  #原始数据录入框
    init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)

    button = Button(window, text="发送邮件", bg="lightblue", width=10,command=SMTP_send.SMTP_send)  # 调用内部方法  加()为直接调用
    button.grid(row=1, column=11)

    window.mainloop() 
if __name__ == '__main__':
    GUI()
