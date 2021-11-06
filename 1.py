from tkinter import *
from tkinter.ttk import *
import os
class MainWindow(Tk):    
    def __init__(self):        
        super().__init__()        
        self.title("主窗体")        
        self.geometry("900x640+180+80")        
        self.resizable(0,0)        
        self["bg"]="skyblue"        
        # 加载gui        
        self.setup_UI()    
    def setup_UI(self):        
        # 设定Style        
        self.Style01 = Style()        
        self.Style01.configure("left.TPanedwindow",background = "navy")        
        self.Style01.configure("right.TPanedwindow", background="skyblue")        
        self.Style01.configure("TButton",width = 10,font = ("华文黑体",15,"bold"))        
        # Top_banner        
        #self.Login_image = PhotoImage(file = "."+os.sep+"img"+os.sep+"stu_main_top_banner.png")        
        #self.Lable_image = Label(self,image = self.Login_image)        
        #self.Lable_image.pack()        
        # 左边：按钮区域,创建一个容器        
        self.Pane_left = PanedWindow(width = 200,height = 540,style = "left.TPanedwindow")        
        self.Pane_left.place(x = 4,y = 94)        
        self.Pane_right = PanedWindow(width=685, height=540,style = "right.TPanedwindow")        
        self.Pane_right.place(x = 210,y = 94)        
        # 添加左边按钮        
        self.Button_add = Button(self.Pane_left,text = "添加学生",style = "TButton")        
        self.Button_add.place(x = 40,y = 20)        
        self.Button_update = Button(self.Pane_left, text="修改学生", style="TButton")        
        self.Button_update.place(x=40, y=45)        
        self.Button_delete = Button(self.Pane_left, text="删除学生", style="TButton")        
        self.Button_delete.place(x=40, y=70)        
        self.Button_modify = Button(self.Pane_left, text="更改密码", style="TButton")        
        self.Button_modify.place(x=40, y=120)        
        # 右边：查询、TreeView

if __name__ == '__main__':    
    this_main = MainWindow()    
    this_main.mainloop()