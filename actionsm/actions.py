"""imports"""
import os
import pygame
import tkinter as tkr
from tkinter import filedialog
import random
from tinytag import TinyTag


"""vars"""
global songlist
global crr_dir
global crr_song
global var
global songtitle
global volume_level
global song_idx
global sh_rp
global sh_rp_label
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
    tinytag(crr_dir + '/' + songlist.get(tkr.ACTIVE))
    pygame.mixer.music.set_volume(volume_level)

def tinytag(address):
    tag = TinyTag.get(address)
    artist= "artist: "
    #tinySongTitle.set(str(tag.title))
    tinySongTitle.set(artist + str(tag.artist))
    album = "album: "
    tinySongalbum.set(album + str(tag.album))

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()
 #   title_label.set

def resume_music():
    pygame.mixer.music.unpause()

def update_volume(vlevel):
    pygame.mixer.music.set_volume(float(vlevel) / 100.0)

def update_label(): #  updates the variable label to show which song is playing
    global index
  #  title_label.set(titles[index])

def shuffle_music(): # selects a random song
    global index
    index = crr_playlist.index(random.choice(crr_playlist))
    #pygame.mixer.music.load(crr_playlist[index])
    sh_rp.set("SHUFFLE")
    pygame.mixer.music.load(crr_dir + '/' + crr_playlist[index])
    pygame.mixer.music.play()

def repeat_music():
    #pygame.mixer.music.stop()
    sh_rp.set("REPEAT")
    pygame.mixer.music.play(-1)

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
    global sh_rp
    global sh_rp_label
    global tinySongTitle
    global tinySongTitle_label
    global tinySongalbum_label
    global tinySongalbum
    var = tkr.StringVar()
    songtitle = ((tkr.Label(player_window, textvariable = var)))
    sh_rp = tkr.StringVar()
    sh_rp_label = ((tkr.Label(player_window, textvariable=sh_rp)))
    tinySongTitle = tkr.StringVar()
    tinySongTitle_label = ((tkr.Label(player_window, textvariable= tinySongTitle )))
    tinySongalbum = tkr.StringVar()
    tinySongalbum_label = ((tkr.Label(player_window, textvariable= tinySongalbum )))

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
  #  update_label()


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
   # update_label()


def place_lists():
    global songtitle
    songtitle.place(x = 0, y = 0)
    sh_rp_label.place(x = 0, y = 140)
    songlist.grid(row = 0, column = 4)
    tinySongTitle_label.place(x=0, y=20)
    tinySongalbum_label.place(x=0, y=40)
