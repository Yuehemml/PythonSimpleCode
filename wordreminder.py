import tkinter as tk
import tkinter.messagebox as tk_mb
import pandas as pd
import numpy.random as ram

class Tkmain:
    def __init__(self, window):
        self.list = []
        self.index = 0
        self.count = 0
        self.fold_flag = True
        
        self.window = window
        self.window.iconbitmap('favicon.ico')
        self.window.title("单词记忆本")
        self.window.geometry("500x300")
        self.window.bind("<Left>", lambda event: self.left_key_press(event))    
        self.window.bind("<Right>", lambda event: self.right_key_press(event))    
        self.window.bind("<f>", lambda event: self.f_key_press(event)) 
        
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(fill="both")

        self.entry_label = tk.Label(self.menu_frame,text="主菜单",font=("微软雅黑",25,"bold"))
        self.entry_label.pack(side="top",pady=(30,20))
        
        self.start_entry_frame = tk.Frame(self.menu_frame,padx=120)
        self.start_entry_frame.pack(fill="x",side="top",pady=(0,10))
        
        self.entry_label = tk.Label(self.start_entry_frame,text="起始序号(1开始):",font=("微软雅黑",10,"normal"))
        self.entry_label.pack(side="left",padx=(0,20))
        
        self.startrow = tk.Entry(self.start_entry_frame,width=8)
        self.startrow.pack(side="left",padx=(0,50))
        
        self.number_entry_frame = tk.Frame(self.menu_frame,padx=120)
        self.number_entry_frame.pack(fill="x",side="top",pady=(0,10))
        
        self.number_label = tk.Label(self.number_entry_frame,text="记忆个数：",font=("微软雅黑",10,"normal"))
        self.number_label.pack(side="left",padx=(0,20))
        
        self.remnum = tk.Entry(self.number_entry_frame,width=12)
        self.remnum.pack(side="left")
        
        self.enter_button = tk.Button(self.menu_frame,text="开始记忆",width=15,command=lambda:self.turn_to_main())
        self.enter_button.pack(side="top",pady=(25,0))
        
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack_forget()
        
        self.number_label = tk.Label(self.main_frame,font=("微软雅黑",15,"normal"))
        self.number_label.pack(pady=(20, 5))

        self.word_frame = tk.Frame(self.main_frame)
        self.word_frame.pack(fill="both")
        
        self.word_label = tk.Label(self.word_frame, height=1,font=("微软雅黑",25,"bold"))
        self.word_label.pack_forget()

        self.fold_label = tk.Label(self.word_frame, height=1,font=("微软雅黑",25,"bold"))
        self.fold_label.pack(fill="both", pady=(0, 5))
        
        self.meaning_label = tk.Label(self.main_frame, wraplength=300,font=("微软雅黑",10,"normal"))
        self.meaning_label.pack(fill="both", pady=(0, 20))
        
        self.fold_button = tk.Button(self.main_frame,width=15,text="遮挡(F)：开",
                                     command=lambda:self.fold_switch())
        self.fold_button.pack(pady=(0,10))

        self.button_frame = tk.Frame(self.main_frame, padx=10)
        self.button_frame.pack(pady=(0,10))

        self.last = tk.Button(self.button_frame, width=15, text="上一个",
                              command=lambda: self.on_button_click("last"))
        self.last.pack_forget()

        self.next = tk.Button(self.button_frame, width=15, text="下一个",
                              command=lambda: self.on_button_click("next"))
        self.next.pack(side="right", padx=(0, 10))
        
        self.dislocate_button = tk.Button(self.main_frame,width=15,text="重置顺序",
                                          command=lambda: self.dislocate())
        self.dislocate_button.pack_forget()
        
    def left_key_press(self,event):
        self.on_button_click("last")
    
    def right_key_press(self,event):
        self.on_button_click("next")
        
    def f_key_press(self,event):    
        self.fold_switch()
        
    def init_main(self):
            self.index=0
            self.number_label.config(text=self.index+1)
            self.word_label.config(text=self.list[0][0])
            self.meaning_label.config(text=self.list[0][1])
            
    def turn_to_main(self):
        db = pd.read_csv("wordlist.csv")
        
        rowmax = db.shape[0]
        
        self.index = int(self.startrow.get()) -1
        self.count = int(self.remnum.get())
        
        if self.index < 0 or rowmax <= self.index + self.count -1 :
            tk_mb.showerror(title="错误",message="该所填数字超出范围！")
            return
        
        self.list = db.iloc[(self.index):(self.index+self.count), [0,1]].values
        
        self.menu_frame.pack_forget()
        self.main_frame.pack(fill="both")
        self.init_main()
    
    def fold_switch(self):
        if self.fold_flag == True:
            self.fold_label.pack_forget()
            self.word_label.pack(fill="both", pady=(0, 5))
            self.fold_button.config(text="遮挡(F)：关")
            self.fold_flag=False
        else:
            self.fold_label.pack(fill="both", pady=(0, 5))
            self.word_label.pack_forget()
            self.fold_button.config(text="遮挡(F)：开")
            self.fold_flag = True
    
    
    def on_button_click(self, text):
        if text == "last":
            if self.index == 0:
                tk_mb.showerror(title="错误",message="此页已是首页！")
                return
            self.index -= 1
        elif text == "next":
            if self.index == self.count - 1:
                tk_mb.showerror(title="错误",message="此页已是尾页！")
                return
            self.index += 1
        
        if self.index == 0:
            self.last.pack_forget()
        else:
            self.last.pack(side="left", padx=(0, 10))
        
        if self.index == self.count - 1:
            self.next.pack_forget()
            self.dislocate_button.pack()
        else:
            self.next.pack(side="right", padx=(0, 10))
            self.dislocate_button.pack_forget()
        self.show()


    def show(self):
        word = self.list[self.index][0]
        meaning = self.list[self.index][1]
        self.number_label.config(text=self.index + 1)
        self.word_label.config(text=word)
        self.meaning_label.config(text=meaning)


    def dislocate(self):
        self.dislocate_button.pack_forget()
        ram.shuffle(self.list)
        self.last.pack_forget()
        self.next.pack(side="right", padx=(0, 10))
        self.init_main()
        
        

root = tk.Tk()
tk_main = Tkmain(root)
root.mainloop()
