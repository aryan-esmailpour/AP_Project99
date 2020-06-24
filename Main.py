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
    pygame.mixer.music.set_volume(VolumeLevel.get())

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def update_volume(vlevel):
    #print(vlevel)
    pygame.mixer.music.set_volume(float(vlevel) / 100.0)

"""volume edit"""
VolumeLevel = tkr.Scale(player_window, from_ = 100, to_ = 0, orient = tkr.VERTICAL, command = update_volume, resolution = 1)
VolumeLevel.set(33)

"""window buttons"""
play_button = tkr.Button(player_window, width = 5, height = 1, text = "PLAY", command = play_music)
stop_button = tkr.Button(player_window, width = 5, height = 1, text = "STOP", command = stop_music)
pause_button = tkr.Button(player_window, width = 5, height = 1, text = "PAUSE", command = pause_music)
resume_button = tkr.Button(player_window, width = 5, height = 1, text = "GO", command = resume_music)


"""song labels"""
var = tkr.StringVar()
songtitle = tkr.Label(player_window, textvariable = var)

"""place features"""
play_button.pack(fill = "x")
stop_button.pack(fill = "x")
pause_button.pack(fill = "x")
resume_button.pack(fill = "x")
VolumeLevel.pack(fill = "x")
songtitle.pack()
songlist.pack(fill = "both", expand = "yes")

"""run"""
player_window.mainloop()
