from pytube import YouTube
from tkinter import *
import tkinter as tk


def downloader():
    
    global res
    res = 0
    
    t_url = t.get("1.0", "end").strip()
    video = YouTube(t_url)

    if res1.get() ==18:
        res=18
    elif res2.get() ==22:
        res=22
    elif res3.get() == 37:
        res=37
        
    
    video_streams = video.streams.filter(file_extension = 'mp4').get_by_itag(res)
    video_streams.download(filename = "Untitled.mp4", output_path = r"C:\Users\Hawei\Desktop")
    Label(root,text="Downloaded Successfully").pack()



root = Tk()
root.title("Fatih's Video Downloader")
root.geometry("450x350")

t = Text(root, height=1,width=45)

h1 = Label(root,   background= "Grey"   ,text="Youtube Video Downloader")
h1.config(font=("Courier", 14))
h2 = Label(root, text="Enter the link to download")
download = Button(text="Download", background= "Green", command=downloader) 
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()
text = StringVar(root, value="YouTube URL")





#Exec Area
h1.pack()
h2.pack()
t.pack()
Checkbutton(text="360p",onvalue=18, offvalue=0, variable=res1).pack()
Checkbutton(text="720p",onvalue=22, offvalue=0, variable=res2).pack()
Checkbutton(text="1080p",onvalue=37, offvalue=0, variable=res3).pack()
download.pack()


root.mainloop()