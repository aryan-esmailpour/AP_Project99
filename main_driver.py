"""imports"""
import os
import pygame
import tkinter as tkr
from tkinter import filedialog
from GUIM.guim import guim
from actionsm import actions
aui = guim()
aui.audio_init()
aui.make_wind()
aui.make_songlist()
aui.update_list()
aui.set_volume()
aui.make_buttons()
aui.song_label()
aui.place_features()
aui.go_run()



