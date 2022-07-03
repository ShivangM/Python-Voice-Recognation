import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("output.wav", "rb")
sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wav = obj.readframes(-1)
obj.close()

t_audio = n_sample/sample_freq
print(t_audio)

signal_array = np.frombuffer(signal_wav, dtype = np.int16)
times = np.linspace(0, t_audio, num = n_sample)
plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()