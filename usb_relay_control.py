# -*- coding: utf-8 -*-
'''
Dec 2020
@author: Luke.Chen
'''
# ======================
# imports
# ======================
from tkinter.constants import CENTER
import serial
import serial.tools.list_ports
import tkinter as tk
import sys
from tkinter import ttk
global com_port
com_port = ""

# 列出可用的com port
ports = serial.tools.list_ports.comports()

# define relay control command bit
on = bytearray(b"\xA0\x01\x01\xA2")
off = bytearray(b"\xA0\x01\x00\xA1")

# Create instance
win = tk.Tk()

# Add a title
win.title("Power Relay Control")
win.geometry("400x200")

# --- functions ---


def serial_ports():
    return [p.device+':'+p.description for p in serial.tools.list_ports.comports()]


def on_select(event=None):
    global com_port
    com_port_strings = event.widget.get()
    com_port = com_port_strings.split(':') [0]  
    print(com_port_strings.split(':')[0])

def update_com_list():
    number_chosen.set("COM Port")
    number_chosen['values'] = [p.device+':'+p.description for p in serial.tools.list_ports.comports()]

        


# Modified Button Click Function


def turn_on_click():
    ser = serial.Serial(com_port, 9600, timeout=0)
    ser.write(on)
    ser.close()
    


def turn_off_click():
    ser = serial.Serial(com_port, 9600, timeout=0)
    ser.write(off)
    ser.close()


def exit_click():
    sys.exit(0)


# Adding Turn ON Button
turn_on = ttk.Button(win, text="Turn ON Power Relay!", command = turn_on_click)

# Adding Turn OFF Button
turn_off = ttk.Button(win, text="Turn OFF Power Relay!", command = turn_off_click)

# Adding exit Button
exit = ttk.Button(win, text="Eixt Program", command = exit_click)

number_chosen = ttk.Combobox(win, values = serial_ports(),postcommand = update_com_list) 
number_chosen.place(relx=0.5, rely=0.5, relwidth=0.6,
                    relheight=0.15, anchor='center')
# assign function to combobox
number_chosen.bind('<<ComboboxSelected>>', on_select)
number_chosen.set("COM Port")

# Button and Label Placement
# <= Place Turn ON Button
turn_on.place(relx=0.3, rely=0.6, anchor=CENTER)

# <= Place Turn OFF Button
turn_off.place(relx=0.7, rely=0.6, anchor=CENTER)

# <= Place Eixt Button
exit.place(relx=0.5, rely=0.85, anchor=CENTER)

# Adding Description Label
label0 = ttk.Label(
    win, text="Select the COM port that the device is plugged in: ")
label0.config(font=("TkDefaultFont", 10))
label0.place(relx=0.5, rely=0.2, anchor=CENTER)

# combobox placement
number_chosen.place(relx=0.5, rely=0.35, anchor=CENTER)


number_chosen.focus()      # Place cursor into COM port selection

# ======================
# Start GUI
# ======================
win.mainloop()
