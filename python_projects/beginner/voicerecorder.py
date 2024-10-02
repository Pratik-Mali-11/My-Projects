import pyaudio
import wave

# Parameters for recording
format1 = pyaudio.paInt16  # Audio format (16-bit resolution)
channels1 = 2               #mono audio:1, stereo audio: 2
rate1 = 44100               # sample rate in Hz
chunk1 = 1024               # Buffer size
record_seconds = 5
output_filename = "myrec2.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=format1, channels=channels1,
                    rate=rate1, input=True,
                    frames_per_buffer=chunk1)

print("Recording started.....")

frames = []

for _ in range(0, int(rate1 / chunk1 * record_seconds)):
    data = stream.read(chunk1)
    frames.append(data)

print("Recording finished...")

stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a WAV file
with wave.open(output_filename, 'wb') as wf:
    wf.setnchannels(channels1)  # Set number of channels (stereo)
    wf.setsampwidth(audio.get_sample_size(format1))  # Set sample width (16-bit)
    wf.setframerate(rate1)  # Set frame rate (44.1kHz)
    wf.writeframes(b''.join(frames))  # Write the audio frames

print(f"Audio saved as {output_filename}")
