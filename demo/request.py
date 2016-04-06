#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Jacky Yu <jacky325@qq.com>'

from Tkinter import *
import urllib,urllib2,uniqid.fun
from json import *
from time import sleep


def http_submit():
    #return 
    #parse parameters
    try:
        param = eval(Parameter.get(0.0, END))
        Parameter.delete(0.0, END)
        Parameter.insert(END, dumps(param, indent = 4)+"\n")
    except:
        if Parameter.get(0.0, END).isspace():
            param = {}
        else:
            ResponsesText.delete(0.0, END)
            ResponsesText.insert(END, "Invalid json parameters")
            return

    #http request
    ResponsesText.delete(0.0, END)
    ResponsesText.insert(END, "Requesting ...")
    master.update()
    try:
        req = urllib2.urlopen(ServerURL.get(), urllib.urlencode(param))
        txt = req.read()
        try:
            txt = dumps(JSONDecoder().decode(txt), indent = 4)
        except:
            pass
    except:
        txt = "Request failure, URL: " + ServerURL.get()
    
    sleep(1)
    ResponsesText.delete(0.0, END)
    ResponsesText.insert(END, txt)
    return
    
def selectAllParameter(event):  
    Parameter.tag_add(SEL, "0.0", END)
    return 'break'

def selectAllResponses(event):  
    ResponsesText.tag_add(SEL, "0.0", END)
    return 'break'


    
#Gui interface 
master = Tk()

#def Gui init
master.title("Http request v1.0")
master.iconbitmap(uniqid.fun.get_cur_path() + '/img/python.ico')
master.resizable(False, False)

#To be center
width  = 1000
height = 800
maxW, maxH = master.maxsize()
posX = (maxW - width)/2
posY = (maxH - height)/2
master.geometry("%dx%d+%d+%d"%(width, height, posX, posY));
#master.state('zoomed')

Label(master, text="ServerURL：", font="bold").grid(row=0)
Label(master, text="Parameter：", font="bold").grid(row=1)
Label(master, text="Responses：", font="bold").grid(row=3)

ServerURL = Entry(master, width = 95, bg = "#cce8cf")
Parameter = Text(master, height=10, width=95, bg = "#cce8cf")


ResponsesFrame    = Frame(master)
ResponsesScollBar = Scrollbar(ResponsesFrame)
ResponsesText     = Text(
    ResponsesFrame, bg = "#cce8cf", fg="#5200f7", height=28, width=92, 
    yscrollcommand = ResponsesScollBar.set
)
ResponsesScollBar.pack(side=RIGHT, fill=Y)
ResponsesScollBar.config(command = ResponsesText.yview)
ResponsesText.pack(side = LEFT, fill = BOTH)


ServerURL.grid(row=0, column=1, padx=10, pady=10)
Parameter.grid(row=1, column=1, padx=10, pady=10)
ResponsesFrame.grid(row=3, column=1, pady=10)

#submit button : row=2
Button(
    master, text='Submit', fg="#ffffff", bg="#21aeba", command=http_submit
).grid(
    row=2, columnspan=2, ipadx=20, pady=10
)

#widget init
ServerURL.insert(END, "http://")
Parameter.insert(END, '{\n\
    "username": "username",\n\
    "password": "password"\n\
}')

#bind event 
Parameter.bind("<Control-Key-a>", selectAllParameter)
Parameter.bind("<Control-Key-A>", selectAllParameter)
ResponsesText.bind("<Control-Key-a>", selectAllResponses)
ResponsesText.bind("<Control-Key-A>", selectAllResponses)

mainloop()
