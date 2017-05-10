import speech_to_text_v1, text_to_speech_v1
import play_audio
import speech_capture

speech_capture.recNow()

print('audio to play now')

new_audio = play_audio.playAudio()

print('no invoke STT')

speech_to_text_v1.STT()

print('do something with it')

text_to_speech_v1.TTS()