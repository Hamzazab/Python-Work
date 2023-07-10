from cProfile import label
from logging import root
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import tkinter as tk

def createWidgets():
      link_label = Label(root, text='Youtube Link',font=('Arial',30,'bold')   #print statement is not work in tkinter we use label function 
                        ,bg='#E8D579')
      link_label.grid(row=1,column=0,padx=5 , pady=5)
      
      root.link_text = Entry(root,width=60,font=34,textvariable=video_link)
      root.link_text.grid(row=1,column=1,pady=5,padx=5)
      
      destination_label = Label(root,text='Destination:' , bg='#E8D579')
      destination_label.grid(row=2,column=0,pady=5,padx=5)
      
      root.destination_text= Entry(root,width=45,textvariable=download_path)
      root.destination_text.grid(row=2,column=1,padx=3,pady=3)
      
      browse_button = Button(root,text='Browse Video', command=browse , width=10,bg='#05E8E0')
      browse_button.grid(row=2 , column=2,padx=1,pady=1)
      
      download_button = Button(root,text='Download Video',command=download_video,width=25 , bg='#05E8E0')
      download_button.grid(row=3,column=1,padx=3,pady=3) 
      
def browse():
      download_dir = filedialog.askdirectory(initialdir='Your Directory Path')
      download_path.set(download_dir)
      
def download_video():
      url = video_link.get()
      folder = download_path.get()
      get_video= YouTube(url)
      get_stream = get_video.streams.get_highest_resolution()
      get_stream.download(folder)
      messagebox.showinfo('Video Downloaded.....'+folder)
      
#create framwork
root = tk.Tk()

#height and width
root.geometry('900x150') 
root.config(bg='black')
root.title('Video Downloader')



video_link = StringVar()
download_path = StringVar()
createWidgets()
                                                          
root.mainloop()       #always add in last when we use tkinter

