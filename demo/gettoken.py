#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Jacky Yu <jacky325@qq.com>'

from Tkinter import *
import os,urllib,urllib2,uniqid.fun
from json import *
from time import sleep

def token_set(msg):
    Token.delete(0, END)
    Token.insert(END, msg)

def http_submit():
    if len(ServerURL.curselection()) == 0:
        token_set("No server URL is selected")
        return
    #return 
    #parse parameters
    try:
        param = {"username":Username.get()}

        filepath = uniqid.fun.get_cur_path()+'/pb.pem'
        if not os.path.isfile(filepath):
            filepath = False
        param['password'] = uniqid.fun.base64_encode(uniqid.fun.encrypt(Password.get(), filepath))
    except:
        token_set("Invalid json parameters")
        return

    #http request
    Token.delete(0, END)
    Token.insert(END, "Requesting ...")
    master.update()
    try:
        req = urllib2.urlopen(ServerURL.get(ServerURL.curselection()), urllib.urlencode(param))
        txt = req.read()
        try:
            txt = JSONDecoder().decode(txt)['obj']['token']
        except:
            pass
    except:
        txt = "Request failure, URL: " +  ServerURL.get(ServerURL.curselection())
   
    sleep(1)
    token_set(txt)
    return

    
def selectAll(Obj):
    index = ServerURL.curselection()
    Obj.select_range(0, END)
    if len(index) == 1:
        ServerURL.select_set(index)
    
def leave(Obj):
    index = ServerURL.curselection()
    if len(index) == 1:
        ServerURL.select_set(index)

def selectAllUsername(event):
    selectAll(Username)
    return 'break'

def selectAllPassword(event):
    selectAll(Password)
    return 'break'

def selectAllToken(event):
    selectAll(Token)
    return 'break'

def leaveUsername(event):
    leave(Username)
    return 'break'

def leavePassword(event):
    leave(Password)
    return 'break'

def leaveToken(event):
    leave(Token)
    return 'break'

    
#Gui interface 
master = Tk()

#def Gui init
master.title("Token request V1.0")
master.iconbitmap(uniqid.fun.get_cur_path() + '/logo.ico')
master.resizable(False, False)

#To be center
width  = 500
height = 280
maxW, maxH = master.maxsize()
posX = (maxW - width)/2
posY = (maxH - height)/2
master.geometry("%dx%d+%d+%d"%(width, height, posX, posY));
#master.state('zoomed')

Label(master, text="ServerURL：", font="bold").grid(row=0)
Label(master, text="Username：", font="bold").grid(row=1)
Label(master, text="Password：", font="bold").grid(row=2)
Label(master, text="Token：", font="bold").grid(row=3)

ServerURL = Listbox(master, width = 40, height = 2, bg = "#cce8cf", selectbackground = 'LightSkyBlue')
Username  = Entry(master, width = 40, bg = "#cce8cf")
Password  = Entry(master, width = 40, bg = "#cce8cf", show = "*")
Token     = Entry(master, width = 40, bg = "#cce8cf")

ServerURL.grid(row=0, column=1, padx=10, pady=20)
Username.grid(row=1, column=1, padx=10, pady=10)
Password.grid(row=2, column=1, padx=10, pady=10)
Token.grid(row=3, column=1, pady=10)
Button( # submit button : row=4
    master, text='确定', fg="#ffffff", bg="#186faa", command=http_submit
).grid(
    row=4, columnspan=2, ipadx=20, pady=10
)

#widget init
ServerURL.insert(END, "http://server1.com/login")
ServerURL.insert(END, "http://server2.com/login")
ServerURL.select_set((0,)) #This only sets focus on the first item.
ServerURL.event_generate("<<ListboxSelect>>")
Username.insert(END, "username")
Password.insert(END, "password")

#bind event
Username.bind("<Control-Key-a>", selectAllUsername)
Username.bind("<Control-Key-A>", selectAllUsername)
Username.bind('<Double-Button-1>', selectAllUsername)
Username.bind('<B1-Motion>', selectAllUsername)
Username.bind('<Leave>', leaveUsername)

Password.bind("<Control-Key-a>", selectAllPassword)
Password.bind("<Control-Key-A>", selectAllPassword)
Password.bind('<Double-Button-1>', selectAllPassword)
Password.bind('<B1-Motion>', selectAllPassword)
Password.bind('<Leave>', leavePassword)

Token.bind("<Control-Key-a>", selectAllToken)
Token.bind("<Control-Key-A>", selectAllToken)
Token.bind('<Double-Button-1>', selectAllToken)
Token.bind('<B1-Motion>', selectAllToken)
Token.bind('<Leave>', leaveToken)

mainloop()
