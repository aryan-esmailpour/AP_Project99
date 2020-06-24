"""imports"""
import os
import pygame
import tkinter as tkr

"""inits"""
pygame.init()
pygame.mixer.init()

"""window"""
player_window = tkr.Tk()
player_window.title("Mammad Music Player ltd.")
player_window.geometry("260x350")

"""playlist"""
os.chdir("/home/aryan/Desktop/APProject/AP_Project99/songs")
print(os.getcwd)
crr_playlist = os.listdir()

"""show playlist"""
songlist = tkr.Listbox(player_window, highlightcolor = "blue", selectmode = tkr.SINGLE)
print(crr_playlist)
for item in crr_playlist:
    idx = 0
    songlist.insert(idx, item)
    idx += 1 

"""song"""
#current_song = "Track 2.wav"

"""actions"""
def play_music():
    pygame.mixer.music.load(songlist.get(tkr.ACTIVE))
    var.set(songlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()


"""window buttons"""
play_button = tkr.Button(player_window, width = 5, height = 3, text = "PLAY", command = play_music)
stop_button = tkr.Button(player_window, width = 5, height = 3, text = "STOP", command = stop_music)

"""song labels"""
var = tkr.StringVar()
songtitle = tkr.Label(player_window, textvariable = var)

"""place features"""
stop_button.pack(fill = "x")
play_button.pack(fill = "x")
songtitle.pack()
songlist.pack(fill = "both", expand = "yes")

"""run"""
player_window.mainloop()
