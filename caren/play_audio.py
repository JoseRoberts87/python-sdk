from os.path import join, dirname
import os

def playAudio(wave_file):
    os.system(join(dirname(__file__), '../resources/' + wave_file + '.wav'))
