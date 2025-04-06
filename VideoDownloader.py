from tkinter import *
import tkinter as tk
import yt_dlp


def downloader():
    global res
    res = 0

    t_url = t.get("1.0", "end").strip()

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': r"C:\Users\Hawei\Desktop\%(title)s.%(ext)s",

        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([t_url])
        for widget in root.pack_slaves():
            if isinstance(widget, Label) and widget.cget("text") == "Downloaded Successfully" :
                widget.destroy()

        Label(root, text="Downloaded Successfully").pack()
    except Exception as e:
        # Shorten the error message for age restriction
        error_message = str(e)
        if "Sign in to confirm your age" in error_message:
            error_message = "Error: Age-restricted video. Use cookies to bypass."
        
        for widget in root.pack_slaves():
            if isinstance(widget, Label) and widget.cget("text") == error_message:
                return  # Exit to avoid dup
        Label(root, text=error_message).pack()

 


root = Tk()
root.title("Fatih's Video Downloader")
root.geometry("700x270")

t = Text(root, height=1,width=45)

h1 = Label(root,   background= "Grey"   ,text="Youtube Video Downloader")
h1.config(font=("Courier", 14))
h2 = Label(root, text="Enter the link to download")
download = Button(text="Download", background= "Green", command=downloader) 
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()
text = StringVar(root, value="YouTube URL")
exit = Button(root, text="Exit", command= root.destroy)





#Exec Area
h1.pack()
h2.pack()
t.pack()
Checkbutton(text="360p",onvalue=18, offvalue=0, variable=res1).pack()
Checkbutton(text="720p",onvalue=22, offvalue=0, variable=res2).pack()
Checkbutton(text="1080p",onvalue=37, offvalue=0, variable=res3).pack()
download.pack()
exit.pack()


root.mainloop()