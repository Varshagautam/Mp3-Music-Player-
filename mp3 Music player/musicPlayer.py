from logging import exception
from pygame import mixer
from tkinter import *
from tkinter import filedialog

#fix volume to 0.5
current_volume=float(0.5)

#fuctions for music player....
def play_song():
    filename=filedialog.askopenfilename(initialdir="C:/",title=" Please select a file")
    current_song=filename
    song_title=filename.split("/")
    song_title=song_title[-1]
    
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green",text="Now Playing: "+str(song_title))
        volume_label.config(fg="green",text="Volume: "+str(current_volume))
    except exception as e:
        print(e)
        song_title_label.config(fg='red',text="Error to playing track song")


#function for reduce volume...
def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red",text="Volume: Muted")
            return
        current_volume=current_volume-float(0.1)
        current_volume=round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green",text="Volume: "+str(current_volume))
    except exception as e:
        print(e)
        song_title_label.config(fg='red',text="Track has not been selected yet")


#function for increase the volume....
def increase_volume():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="green",text="Volume: Max")
            return
        current_volume=current_volume+float(0.1)
        current_volume=round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green",text="Volume: "+str(current_volume))
    except exception as e:
        print(e)
        song_title_label.config(fg='red',text="Track has not been selected yet")


#function for resume...
def pause():
    try:
        mixer.music.pause()
    except exception as e:
        print(e)
        song_title_label.config(fg='red',text="Track has not been selected yet")


#function for resume...
def resume():
    try:
        mixer.music.unpause()
    except exception as e:
        print(e)
        song_title_label.config(fg='red',text="Track has not been selected yet")
    
    
#main screen....
screen = Tk()
screen.title("Music Player")


#labels...
Label(screen,text=" Custom Music Player ", font=('Arial',15),fg="red").grid(sticky="N",row=0,padx=120)
Label(screen,text=" Select Music To Player ", font=('Arial',11),fg="blue").grid(sticky="N",row=1)
Label(screen,text=" Volume ", font=('Arial',11),fg="red").grid(sticky="N",row=4)
song_title_label=Label(screen,font=("Arial",11))
song_title_label.grid(sticky="N",row=3)
volume_label=Label(screen,font=("Arial",11))
volume_label.grid(sticky="N",row=5)


#button....
Button(screen,text="Select Song",font=("Arial",11),command=play_song).grid(row=2,sticky="N")
Button(screen,text="Pause",font=("Arial",11),command=pause).grid(row=3,sticky="E")
Button(screen,text="Resume",font=("Arial",11),command=resume).grid(row=3,sticky="W")
Button(screen,text="-",font=("Arial",11),width=5,command=reduce_volume).grid(row=5,sticky="W")
Button(screen,text="+",font=("Arial",11),width=5,command=increase_volume).grid(row=5,sticky="E")


screen.mainloop()

