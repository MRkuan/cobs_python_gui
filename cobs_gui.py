#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author ：Kuan
# GUI         ref:http://blog.csdn.net/liuxu0703/article/details/60781107
# arithmetic  ref:https://my.oschina.net/Cw6PKk/blog/750067
# issue ：http://blog.csdn.net/sixtyfour/article/details/14109153
# function ：http://blog.csdn.net/crylearner/article/details/38521685
#            http://blog.csdn.net/robinchenyu/article/details/8989791
from tkinter import *
import ctypes  
import os
import tkinter.messagebox as messagebox

#cobs dll
cobs_dll =  ctypes.cdll.LoadLibrary("cobs.dll")   

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        Label(self,text="InputData").grid(row=0)
        Label(self,text="OutPutData").grid(row=1)

        self.InputData=Entry(self,text="111",width=400)
        self.InputData.grid(row=0, column=1)

        self.OutPutData=Entry(self,text="222",width=400)
        self.OutPutData.grid(row=1, column=1)

        self.StuffButton = Button(self, text='Stuff', command=self.Stuff)
        self.StuffButton.grid(row=2, column=0, sticky=W)

        self.UnStuffButton = Button(self, text='UnStuff', command=self.UnStuff)
        self.UnStuffButton.grid(row=2, column=1, sticky=W)

        self.ClearButton = Button(self, text='clear', command=self.clear)
        self.ClearButton.grid(row=3, column=0, sticky=W)

        self.About = Button(self, text='about', command=self.about)
        self.About.grid(row=3, column=1, sticky=W)

    def clear(self):
        self.InputData.delete(0,END)
        self.OutPutData.delete(0,END)
        self.InputData.focus()

    def Stuff(self):
        try:
            input_bytes=bytes.fromhex(self.InputData.get().replace(' ', ''))
            input_bytes_len=len(input_bytes)
            output_bytes=bytes(input_bytes_len+1)
            cobs_dll.StuffData(input_bytes,input_bytes_len,output_bytes)
            tmp=''.join( [ "%02X " % x for x in output_bytes ] ).strip()
            self.OutPutData.delete(0,END)
            self.OutPutData.insert(0,tmp)
            self.OutPutData.focus()
        except Exception as e:
            messagebox.showerror('Message',e)
            self.OutPutData.delete(0,END)
            self.InputData.focus()
        finally:
            None 

    def UnStuff(self):
        try:
            input_bytes=bytes.fromhex(self.InputData.get().replace(' ', ''))
            input_bytes_len=len(input_bytes)
            output_bytes=bytes(input_bytes_len-1)
            cobs_dll.UnStuffData(input_bytes,input_bytes_len,output_bytes)
            tmp=''.join( [ "%02X " % x for x in output_bytes ] ).strip()
            self.OutPutData.delete(0,END)
            self.OutPutData.insert(0,tmp)
            self.OutPutData.focus()
        except Exception as e:
            messagebox.showerror('Message',e)
            self.OutPutData.delete(0,END)
            self.InputData.focus()
        finally:
            None 
        None

    def about(self):
        messagebox.showinfo('Message', 'COBSforToN TOOL   \n power by tkinter')
        cobs_dll.StuffData

app = Application()

app.master.title('COBSforToN')

width ,height= 400, 120

app.master.geometry('%dx%d+%d+%d' % (width,height,(app.winfo_screenwidth() - width ) / 2, (app.winfo_screenheight() - height) / 2))

app.master.maxsize(1500,height)

app.master.minsize(width,height)

app.mainloop()