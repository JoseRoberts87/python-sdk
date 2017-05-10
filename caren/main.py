import speech_to_text_v1, text_to_speech_v1
import play_audio
import speech_capture
import time

pause = time.sleep(2)

def oFile(text_file):
    n_text_file = open(text_file, 'r')
    rLine = n_text_file.readline()
    return rLine

speech_capture.recNow()

print('audio to play now')

text_to_speech_v1.TTS(oFile('../resources/text_files/acknowledge.txt'))
play_audio.playAudio('output')
pause

play_audio.playAudio('speech')

print('no invoke STT')

# speech_to_text_v1.STT()

print('do something with it')


time.sleep(4)

text_to_speech_v1.TTS(oFile('../resources/text_files/confirm.txt'))
play_audio.playAudio('output')
pause

text_to_speech_v1.TTS(oFile('../resources/text_files/standby.txt'))
print('audio to play now')

play_audio.playAudio('output')