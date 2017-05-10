from os.path import join, dirname
import os

def playAudio():
    os.system(join(dirname(__file__), '../resources/speech.wav'))
