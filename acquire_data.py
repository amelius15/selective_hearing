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

max_points = 10000

index = 1

data_set = None

label = 'ANTHONY'

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = np.fromstring(in_data, 'Float32')
    global index
    global data_set

    data_i = np.arange(len(data))
    mask = np.isfinite(data)
    filtered_data = np.interp(data_i, data_i[mask], data[mask])

    fft_data = np.fft.fft(filtered_data)
    real_fft = np.absolute(fft_data)
    real_fft /= np.max(np.abs(real_fft),axis=0)
    if data_set is not None:
        data_set = np.vstack((data_set, real_fft))
    else:
        data_set = real_fft
    index += 1
    if index % 1000 == 0:
        print(index)
    if False:
        return (in_data, pyaudio.paContinue)
    else:
        return (np.zeros(len(data)), pyaudio.paContinue)
time.sleep(1)
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback,
                frames_per_buffer=FRAMESIZE)
stream.start_stream()

while stream.is_active() and index<max_points:
    time.sleep(0.001)
np.save(str(max_points) + '_' + str(RATE) + '_' + str(FRAMESIZE) + '_' + label, data_set)
stream.stop_stream()
stream.close()

p.terminate()
