"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
This is the callback (non-blocking) version.
"""

import pyaudio
import time
import numpy as np

FRAMESIZE = 512
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = np.fromstring(in_data, 'Float32')
    print(len(data))

    # data has NaNs in it; filter them out
    data_i = np.arange(len(data))
    mask = np.isfinite(data)
    filtered_data = np.interp(data_i, data_i[mask], data[mask])

    fft_data = np.fft.fft(filtered_data)
    print(fft_data)
    if False:
        return (in_data, pyaudio.paContinue)
    else:
        return (np.zeros(len(data)), pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback,
                frames_per_buffer=FRAMESIZE)
# print (stream.format)
stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()
