import torch
import sounddevice as sd
import time
import torchaudio
import torchaudio

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'
put_accent = True
put_yo = True
device = torch.device('cpu')
text = "hello"
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)

text=example_text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)
print(text)

sd.play(audio, sample_rate)
time.sleep(len(audio)/sample_rate)
sd.stop()
