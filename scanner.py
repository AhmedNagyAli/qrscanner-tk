import cv2
from pyzbar.pyzbar import decode
import time
from tkinter import *
import tkinter as tk
from tkinter.font import BOLD
from PIL import ImageTk,Image


def capture():
    camm = cv2.VideoCapture(0)
    camm.set(5,640)
    camm.set(6,480)
    camera = True
    while camera == True:
        succeess, frame = camm.read()
    
        for i in decode(frame):
            print(i.type)
            print(i.data.decode('utf-8'))
            time.sleep(5)
            cv2.imshow("QurQr_code_Scanner", frame)
            cv2.waitKey(3)
            
            
root = tk.Tk()
root.title("Code Scane")
root.geometry('800x800')
root.config(bg='#262526')


canvas = Canvas(root, width = 600, height = 600)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("/home/granada3/_Dev/qr_scanner/na.jpeg"),size=(500,500))
#img = img.size(250,250, Image.ANTIALIAS)
canvas.create_image(10, 10, anchor=NW, image=img)

slabel = tk.Label(root, text="Open The Camera to scane the code")
slabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 12), padx=10,pady=15)
slabel.pack()



btn = tk.Button(root, text='OPEN', width=60,height=1 ,bg="#1b1b1b",command=capture)
btn.config(fg='#f4f4f4',font=("Helvetica", 12, BOLD), padx=50,pady=15, borderwidth=1)
btn.pack(pady= 50, padx= 15)



root.mainloop()