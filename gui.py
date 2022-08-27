from cgitb import text
from distutils.command.bdist import show_formats
import tkinter as tk 
from tkinter import Canvas, StringVar, ttk
from tkinter import W,E,S,N
from tkinter import messagebox as mb 
import numpy as np 
from algo import Sort

class GUI():
    def __init__(self,window) -> None:
        self.root = window 
        self.content = ttk.Frame(self.root)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.content.rowconfigure(0,weight=1)
        self.content.columnconfigure(0,weight=1)
        self.sort = Sort()

    def setWindow(self):
        self.root["width"] = 600 
        self.root["height"] = 600
        
        #layout 
        self.content.grid(column=0,row=0
            ,sticky="news")
    
    def setInputFrame(self):
        self.inputFrame = ttk.LabelFrame(self.content,text="Input")
        self.inputArr = tk.StringVar()
        self.inputEntry = tk.Entry(self.inputFrame,textvariable=self.inputArr)
        self.inputLabel = ttk.Label(self.inputFrame,text="Input Your Array")
        self.inputArrLabel = tk.Label(textvariable=self.inputArr)
        def rand():
            length = 20 
            randArr = np.random.randint(1,100,(length,))
            s = ""
            for i in range(length):
                s += str(randArr[i]) + " "
            
            self.inputArr.set(s)

        self.inputRandomButton = tk.Button(self.inputFrame,text="Random",command=rand)

        def parse():
            # 字符串解析为数组
            arrStr = self.inputArr.get() 
            return arrStr.strip().split(" ")


        self.mode = tk.StringVar(value="insert")
        self.inputCombo = ttk.Combobox(self.inputFrame,textvariable=self.mode,value=("insert","halfInsert","hill","bubble","quick","choose"))

        def encode(arr):
            string = ""
            for s in arr: 
                string += str(s) 
                string += " " 
            return string

        def confirmCommand():
            # 完成输入
            # self.sort.arr = np.array(parse())
            self.sort.initArr(np.array(parse()))
            self.sort.reset() 
            self.sort.mode = self.mode.get()
            self.origArrText.set(encode(self.sort.arr))
            self.currentArrText.set(self.origArrText.get())
            self.prevArrText.set(self.origArrText.get())

        self.confirmButton = tk.Button(self.inputFrame,text="Confirm",command=confirmCommand)
        def stepCommand():
            # 运行一次计算
            self.sort.nextstep()
            self.prevArrText.set(encode(self.sort.prevArr))
            self.currentArrText.set(encode(self.sort.arr))
            self.stepCnt.set(str(self.sort.step))

        self.stepButton = tk.Button(self.inputFrame,text="Step",command=stepCommand)

        # layout 
        self.inputFrame.grid(column=0,row=0,sticky="news")
        self.inputLabel.grid(column=0,row=0,sticky="nws")
        self.inputEntry.grid(column=0,row=1,columnspan=2,sticky="news")
        self.inputArrLabel.grid(column=0,row=3, sticky="nws")
        self.inputRandomButton.grid(column=0,row=4,sticky="nws")
        self.confirmButton.grid(column=1,row=4,sticky="nws")
        self.stepButton.grid(column=0,row=5,sticky="nws")
        self.inputCombo.grid(column=0,row=2,sticky="news")
    
    def setDisplayPanel(self):
        self.showFrame = tk.LabelFrame(self.content,text="Display")
        self.origArrText = tk.StringVar()
        self.label1 = tk.Label(self.showFrame,text="Original Arr")
        self.origArr = tk.Label(self.showFrame,textvariable=self.origArrText)
        self.label2 = tk.Label(self.showFrame, text = "Previous Arr")
        self.prevArrText = tk.StringVar()
        self.prevArr = tk.Label(self.showFrame,textvariable=self.prevArrText)
        self.label3 = tk.Label(self.showFrame,text="Current Arr")
        self.currentArrText = tk.StringVar()
        self.currentArr = tk.Label(self.showFrame,textvariable=self.currentArrText)
        self.stepCnt = tk.StringVar()
        self.subFrame = tk.Frame(self.showFrame)
        self.label4 = tk.Label(self.subFrame,text="Step: ")
        self.stepLabel = tk.Label(self.subFrame,textvariable=self.stepCnt)

        # layout 
        self.showFrame.grid(column=1,row=0,sticky="news")
        self.label1.grid(column=0,row=0,sticky="nws")
        self.origArr.grid(column=0,row=1,sticky="nws")
        self.label2.grid(column=0,row=2,sticky="nws")
        self.prevArr.grid(column=0,row=3,sticky="nws")
        self.label3.grid(column=0,row=4,sticky="nws")
        self.currentArr.grid(column=0,row=5,sticky="nws")
        self.subFrame.grid(column=0,row=6,sticky="news")
        self.label4.grid(column=0,row=0,sticky="nws")
        self.stepLabel.grid(column=1,row=0,sticky="nws")
    
    def run(self):
        self.setWindow()
        self.setInputFrame()
        self.setDisplayPanel()
        self.root.mainloop()
    
if __name__ == "__main__":
    window = tk.Tk() 
    window.title("Sorting")
    gui = GUI(window)
    gui.run()