from tkinter import *
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
import os
import pygame
root = Tk()
root.title("instahub")
root.resizable(False,False)
fileInput = StringVar()

def fileSelect():
    global video,path
    video = filedialog.askopenfilename(initialdir="/", title="Select video file")
    head, tail = os.path.split(video)
    name_of_project = ((os.path.splitext(tail))[0])
    path = os.path.join(head, name_of_project+"....instahub")
    fileInput.set(tail)
def go():
    clip = VideoFileClip(video)
    time = clip.duration
    num_of_parts_60 = time//60
    last_part = time % 60
    start = 0
    os.mkdir(path)
    for part in range(int(num_of_parts_60)):
        ffmpeg_extract_subclip("game.mp4", start, start+60,
                            targetname=f"{path}\\{part+1}.mp4")
        start += 60
    if last_part != 0:
        ffmpeg_extract_subclip("game.mp4", start, start+last_part,
                            targetname=f"{path}\\{int(num_of_parts_60)+1}.mp4")

def show():
    pygame.display.set_caption('Show Video')
    showclip = VideoFileClip(video)
    showclip.preview()
    pygame.quit()


txtDisplay = Entry(root, font=('arial', 20, 'bold'), textvariable=fileInput, bd=30,
                   insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)
Select = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
                text='Select', command=fileSelect).grid(row=1, column=0)
Show = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
              text='Show', command=show).grid(row=1, column=1)
GO = Button(root, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='Go', command=go).grid(row=1, column=2)


root.mainloop()
