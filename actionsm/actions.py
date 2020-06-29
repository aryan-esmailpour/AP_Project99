"""imports"""
import os
import pygame
import tkinter as tkr
from tkinter import filedialog

"""vars"""
global songlist
global crr_dir
global var
global songtitle
global volume_level
global song_idx
volume_level = 0.33
isfolder = 0
song_idx = 0
crr_playlist = []

"""inits"""
def pygame_init():
    pygame.init()
    pygame.mixer.init()

"""main funcs"""
def playlist_init(tmp_dir):
    global crr_playlist
    crr_playlist.clear()
    all_list = os.listdir(tmp_dir)
    for item in all_list:
        if item.endswith(".wav") or item.endswith(".mp3"):
            crr_playlist.append(item)

def chng(v):
    global volume_level
    volume_level = float(v) / 100.0
    pygame.mixer.music.set_volume(volume_level)
    
def make_songlist(player_window):
    global songlist
    songlist = tkr.Listbox(player_window, highlightcolor = "blue", selectmode = tkr.SINGLE)

def update_songlist():
    songlist.delete(0,'end')
    idx = 0
    for item in crr_playlist:
        songlist.insert(idx, item)
        idx += 1

def play_music():
    global var
    global crr_dir
    global songlist
    global song_idx
    pygame.mixer.music.stop()
    crr_song = songlist.get(tkr.ACTIVE)
    print(crr_song)
    ind = 0
    for item in crr_playlist:
        if item == crr_song:
            print(ind)
            break
        ind += 1
    song_idx = ind    
    pygame.mixer.music.load(crr_dir + '/' + songlist.get(tkr.ACTIVE))
    var.set(songlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume_level)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def update_volume(vlevel):
    pygame.mixer.music.set_volume(float(vlevel) / 100.0)

def dir_load():
    global crr_dir
    global songlist
    global isfolder
    isfolder = 1
    crr_dir = filedialog.askdirectory()
    playlist_init(crr_dir)
    update_songlist()

def next_load():
    global songlist
    global isfolder
    global sng_idx
    if isfolder == 1:
        songlist.delete(0,'end')
        isfolder = 0
        sng_idx = 0
    h = filedialog.askopenfilename()
    name = ""
    sz = len(h)
    idx = sz
    for i in range(sz - 1, 0, -1):
        if h[i] == '/':
            break
        idx -= 1
    for i in range(idx, len(h)):
        name += h[i]
    songlist.insert(sng_idx, name)
    pygame.mixer.music.queue(h)
    sng_idx += 1

def set_songtitle(player_window):
    global var
    global songtitle
    var = tkr.StringVar()
    songtitle = ((tkr.Label(player_window, textvariable = var)))

def next_song():
    global song_idx
    global songlist
    num = len(crr_playlist)
    song_idx += 1
    song_idx %= num
    songlist.selection_clear(0, 'end')
    songlist.select_set(song_idx)
    songlist.activate(song_idx)
    play_music()

def prev_song():
    global song_idx
    global songlist
    num = len(crr_playlist)
    song_idx += num
    song_idx -= 1
    song_idx %= num
    songlist.selection_clear(0, 'end')
    songlist.select_set(song_idx)
    songlist.activate(song_idx)
    play_music()

def place_lists():
    global songtitle
    songtitle.place(x = 0, y = 0)
    songlist.grid(row = 0, column = 4)

