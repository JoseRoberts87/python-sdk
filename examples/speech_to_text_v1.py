import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='fe23acf3-7b7e-409a-8d31-99347fbe3f12',
    password='CWwugKeGzVIk',
    x_watson_learning_opt_out=False
)

# print(json.dumps(speech_to_text.models(), indent=2))
#
# print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), '../resources/speech.wav'),
          'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=True,
        word_confidence=True),
        indent=2))
