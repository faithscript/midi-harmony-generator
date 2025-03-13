import pygame

pygame.init()
pygame.mixer.music.load("midi_work/isolated_track.mid")
pygame.mixer.music.play()

input("Press Enter to stop playback...")
pygame.mixer.music.stop()

'''
explanation:
importing the library and initializing all the modules
mixer.music.load loads the music file into pygame
then mixer.music.plau plays the midi file
'''