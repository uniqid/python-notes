#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Jacky Yu <jacky325@qq.com>'

import os, uniqid.fun
from time import sleep
from Tkinter import *

class DirList(object):
    def __init__(self, initdir = None):
        #set window
        self.window = Tk()
        self.window.title("Directory list V1.0")
        self.window.resizable(False, False)
        self.window.geometry('500x420')
        self.window.iconbitmap(uniqid.fun.get_cur_path() + '/img/python.ico')
        
        self.frameDirList         = Frame(self.window)
        self.frameDirListScollBar = Scrollbar(self.frameDirList)
        self.frameDirListScollBar.pack(side=RIGHT, fill=Y)
        self.frameDirList.pack()
        self.listboxDirList = Listbox(
            self.frameDirList,
            height = 15,
            width  = 50,
            bg = "#cce8cf",
            yscrollcommand = self.frameDirListScollBar.set
        )
        self.listboxDirList.bind('<Double-Button-1>', self.setDirAndList)
        self.listboxDirList.config(selectbackground = 'LightSkyBlue')
        self.frameDirListScollBar.config(command = self.listboxDirList.yview)
        self.listboxDirList.pack(side = LEFT, fill = BOTH)

        #error message
        self.errLabel = Label(self.window, fg='red', font=('Helvetica',12,'normal'))
        self.errLabel.pack()
        
        self.iptTxt = StringVar(self.window)
        self.iptDir = Entry(self.window, width = 50, textvariable = self.iptTxt)
        self.iptDir.bind('<Return>', self.ListDir)
        self.iptDir.pack()
        
        #buttons
        self.frameBnts = Frame(self.window)
        self.btn_ls    = Button(
            self.frameBnts,
            text             = 'List Directory',
            command          = self.ListDir,
            activeforeground = 'white',
            activebackground = 'green'
        )
        self.btn_clr   = Button(
            self.frameBnts,
            text             = 'Clear',
            command          = self.clrDir,
            activeforeground = 'white',
            activebackground = 'blue'
        )
        self.btn_quit  = Button(
            self.frameBnts,
            text             = 'Quit',
            command          = self.window.quit,
            activeforeground = 'white',
            activebackground = 'red'
        )
        self.btn_ls.pack(side = LEFT)
        self.btn_clr.pack(side = LEFT)
        self.btn_quit.pack(side = LEFT)
        self.frameBnts.pack()

        if initdir: #comment none
            self.iptTxt.set(initdir)
            self.ListDir()

    def clrDir(self, ev=None):
        self.errLabel.config(text = '')
        self.listboxDirList.delete(0, END)
        self.iptTxt.set('')

    def setDirAndList(self, ev=None):
        selected = self.listboxDirList.get(self.listboxDirList.curselection())
        if not selected:
            return
        paths = os.getcwd()+"\\"+selected
        self.iptTxt.set(paths)
        if not os.path.isdir(paths):
            self.errLabel.config(text = selected + ': not a directory')
            self.window.update()
            return
        self.ListDir()

    def ListDir(self, ev = None):
        paths  = self.iptTxt.get()
        if not paths: paths = os.curdir

        errMsg = ''
        if not os.path.exists(paths):
            errMsg = 'No such directory'
        elif not os.path.isdir(paths):
            errMsg = 'Not a directory'

        if errMsg:
            self.errLabel.config(text = errMsg)
        else:
            os.chdir(paths)
            self.iptTxt.set(os.getcwd())

            self.listboxDirList.delete(0, END)
            self.listboxDirList.insert(END, os.curdir)

            dirlist = os.listdir(os.curdir)
            dirlist.sort()
            for eachFile in dirlist:
                self.listboxDirList.insert(END, eachFile)
        self.window.update()

def main():
    DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
