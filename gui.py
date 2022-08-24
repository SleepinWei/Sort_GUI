import tkinter as tk 
from tkinter import Canvas, StringVar, ttk
from tkinter import W,E,S,N
from tkinter import messagebox as mb 
import numpy as np 

class GUI():
    def __init__(self,window) -> None:
        self.root = window 
        self.content = ttk.Frame(self.root)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.content.rowconfigure(0,weight=1)
        self.content.columnconfigure(0,weight=1)
    
    