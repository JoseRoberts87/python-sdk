# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

def TTS():
    text_to_speech = TextToSpeechV1(
        username='2f06cca7-e165-4d01-8740-6fe83661805a',
        password='wwl2Nrrb8iae',
        x_watson_learning_opt_out=True)  # Optional flag

    with open(join(dirname(__file__), '../resources/output.wav'),
              'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize('Hello baby Jose, how are you? do you want to play rescue bots?', accept='audio/wav',
                                      voice="en-US_AllisonVoice"))
