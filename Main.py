"""imports"""
import pygame
import tkinter as tkr

"""song"""
current_song = "/home/aryan/Desktop/APProject/AP_Project99/songs/Track 2.wav"

"""actions"""
def play_music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

"""window"""
player_window = tkr.Tk()
player_window.title("Mamad Music Player ltd.")
player_window.geometry("260x350")

"""window buttons"""
play_button = tkr.Button(player_window, width = 5, height = 3, text = "PLAY", command = play_music)
play_button.pack(fill = "x")
stop_button = tkr.Button(player_window, width = 5, height = 3, text = "STOP", command = stop_music)
stop_button.pack(fill = "x")

"""song labels"""
label1 = tkr.LabelFrame(player_window, text = "Song Name")
label1.pack(fill = "both", expand = "yes")
contents1 = tkr.Label(label1, text = "Song.wav")
contents1.pack()


"""run"""
player_window.mainloop()
