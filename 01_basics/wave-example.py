from traceback import FrameSummary
import wave

obj = wave.open("output.wav", "rb")

# print("Number of channels", obj.getnchannels())
# print("Sample Width", obj.getsampwidth())
# print("Frame Rate", obj.getframerate())
# print("Number Of Frames", obj.getnframes())
# print("Parameters", obj.getparams())

time = obj.getnframes() / obj.getframerate()
print("Time", time)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("new_output.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)
obj_new.writeframes(frames)

obj_new.close()
