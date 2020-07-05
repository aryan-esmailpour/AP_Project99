"""imports"""
import os
import pygame
import tkinter as tkr
from actionsm import actions


class guim:

    def __init__(self):
        self.tit = "Mammad Music Player"
        self.sz = "438x315"

    def audio_init(self):
        actions.pygame_init()

    def make_wind(self):
        self.wind = tkr.Tk()
        self.wind.title(self.tit)
        self.wind.geometry(self.sz)

    def make_list(self):
        actions.make_songlist(self.wind)

    def update_list(self):
        actions.update_songlist()

    def make_buttons(self):
        self.play_button = tkr.Button(self.wind, width=5, height=1, text="PLAY", command=actions.play_music)
        self.stop_button = tkr.Button(self.wind, width=5, height=1, text="STOP", command=actions.stop_music)
        self.pause_button = tkr.Button(self.wind, width=5, height=1, text="PAUSE", command=actions.pause_music)
        self.resume_button = tkr.Button(self.wind, width=5, height=1, text="RESUME", command=actions.resume_music)
        self.browse_button = tkr.Button(self.wind, width=5, height=1, text="Browse...", command=actions.dir_load)
        self.queue_button = tkr.Button(self.wind, width=5, height=1, text="play next", command=actions.next_load)
        self.next_button = tkr.Button(self.wind, width=5, height=1, text="next", command=actions.next_song)
        self.prev_button = tkr.Button(self.wind, width=5, height=1, text="prev", command=actions.prev_song)
        self.repeat_button = tkr.Button(self.wind, width=5, height=1, text="REPEAT", command=actions.repeat_music)
        self.shuffle_button = tkr.Button(self.wind, width=5, height=1, text="shuffle", command=actions.shuffle_music)

    def go_run(self):

        self.wind.mainloop()

    def make_songlist(self):
        actions.make_songlist(self.wind)

    def place_features(self):
        self.play_button.grid(row=1, column=0)
        self.stop_button.grid(row=1, column=1)
        self.pause_button.grid(row=1, column=2)
        self.resume_button.grid(row=1, column=3)
        self.repeat_button.grid(row=2, column=3)
        self.shuffle_button.grid(row=3, column=0)
        self.VolumeLevel.grid(row=0, column=3, sticky='nse')
        actions.place_lists()
        self.browse_button.grid(row=1, column=4, sticky='nwse')
        self.queue_button.grid(row=2, column=0, sticky='wens')
        self.next_button.grid(row=2, column=1, sticky='nwse')
        self.prev_button.grid(row=2, column=2, sticky='wens')

    def update_vlc(self, VL):
        actions.chng(self.VolumeLevel.get())

    def set_volume(self):
        self.VolumeLevel = tkr.Scale(self.wind, from_=100, to_=0, orient=tkr.VERTICAL, command=self.update_vlc,
                                     resolution=1)
        self.VolumeLevel.set(33)

    def song_label(self):
        actions.set_songtitle(self.wind)


