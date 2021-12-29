import os # to fetch songs and directories
from tkinter.filedialog import askdirectory # for selecting our song directory
import pygame # for playing music
from mutagen.id3 import ID3 # For tagging the meta data to our songs
from tkinter import * # for UI
from PIL import ImageTk, Image
root = Tk() # creates an Empty window
root.title("MUSIC PLAYER")
root.geometry("600x400+10+10")
root.config(bg="black")
root.minsize(800,400) # set size as 300 x 300 wide, Change this accordingly
listofsongs = []
realnames = []
global index
index = 0 # for choosing the first song
def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(file)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play() 

def nextsong(event):
    global index
    global v
    try:
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index = 0 #to ensure that the songsplay in a cycle
        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.play()
        
def prevsong(event):
    global index
    global v
    try:
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index = len(realnames)-1
        
def stopsong(event):
 # stop the current song which is playing
 pygame.mixer.music.stop()
 # set our Label to empty
    




label = Label(root,text='Music Player',width=20,font=('arial',28,"bold"),background="cadet blue",fg="gold")# set the heading
label.place(x = 10,y = 10)
directorychooser()
#make a ListBox to store all our songs list.
#So that user can know what’s coming next
listbox = Listbox(root,width =65,font=('arial',10,"bold"),background="black",fg="gold")
listbox.place(x = 10,y = 60)

realnames.reverse()
print(realnames)
for items in realnames:
     listbox.insert(0,items)
     
nextbutton = Button(root,text = 'Next Song',width = 16,font=('MonotypeCorsiva',16,"bold"),fg="blue")
nextbutton.place(x=20,y=290)

previousbutton = Button(root,text = 'Previous Song',width=16,font=('MonotypeCorsiva',16,"bold"),fg="blue")
previousbutton.place(x=240,y=290)

stopbutton = Button(root,text='Stop Music',width=26,font=('MonotypeCorsiva',16,"bold"),fg="blue")
stopbutton.place(x=40,y=350)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

canv = Canvas(root, width=200, height=200, bg='black',highlightthickness=0)
canv.place(x = 500,y = 50)
photo = ImageTk.PhotoImage(Image.open('image.jpg'))
photolabel = Label(root, image=photo, text="") # attaching image to thelabel
photolabel.place(x=550, y=96)
canv.create_image(20, 20, anchor=NW)
root.mainloop()
