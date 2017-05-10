# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='2f06cca7-e165-4d01-8740-6fe83661805a',
    password='wwl2Nrrb8iae',
    x_watson_learning_opt_out=True)  # Optional flag

# print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), '../resources/output.wav'),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize('Hello baby Jose, how are you? do you want to play rescue bots?', accept='audio/wav',
                                  voice="en-US_AllisonVoice"))

# print(
#     json.dumps(text_to_speech.pronunciation(
#         'Watson', pronunciation_format='spr'), indent=2))
#
# print(json.dumps(text_to_speech.customizations(), indent=2))

# print(json.dumps(text_to_speech.create_customization('test-customization'),
#  indent=2))

# print(text_to_speech.update_customization('YOUR CUSTOMIZATION ID',
# name='new name'))

# print(json.dumps(text_to_speech.get_customization('YOUR CUSTOMIZATION ID'),
#  indent=2))

# print(json.dumps(text_to_speech.get_customization_words('YOUR CUSTOMIZATION
#  ID'), indent=2))

# print(text_to_speech.add_customization_words('YOUR CUSTOMIZATION ID',
#                                              [{'word': 'resume',
# 'translation': 'rɛzʊmeɪ'}]))

# print(text_to_speech.set_customization_word('YOUR CUSTOMIZATION ID',
# word='resume',
#                                             translation='rɛzʊmeɪ'))

# print(json.dumps(text_to_speech.get_customization_word('YOUR CUSTOMIZATION
# ID', 'resume'), indent=2))

# print(text_to_speech.delete_customization_word('YOUR CUSTOMIZATION ID',
# 'resume'))

# print(text_to_speech.delete_customization('YOUR CUSTOMIZATION ID'))
