"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
This is the callback (non-blocking) version.
"""

import pyaudio
import time
import numpy as np
import pickle
import sys
from cStringIO import StringIO
import logging
import os

sys.stdout = StringIO()
logging.basicConfig(
            format="%(message)s",
            level=logging.ERROR,
            stream=sys.stdout)
logging.getLogger("sknn").setLevel(logging.ERROR)

FRAMESIZE = 512
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

fs = open('nn_fire_a.pkl', 'rb')
nn_fire = pickle.load(fs)
fs.close()

fs = open('nn_justine.pkl', 'rb')
nn_justine = pickle.load(fs)
fs.close()

fs = open('nn_anthony.pkl', 'rb')
nn_anthony = pickle.load(fs)
fs.close()

fs = open('nn_combined.pkl', 'rb')
nn_combined = pickle.load(fs)
fs.close()

fs = open('nn_anthony_vs_justine.pkl', 'rb')
nn_ant_v_just = pickle.load(fs)
nn_ant_v_just.verbose = False
fs.close()

ID_FIRE = True
ID_ANTHONY = False
ID_JUSTINE = False
<<<<<<< HEAD
count = 0
=======

>>>>>>> bee59e5... much more stuff than you should have in one commit
def callback(in_data, frame_count, time_info, status):
    # global nn
    global ID_JUSTINE
    global ID_ANTHONY
    global ID_FIRE
    global nn_fire
    global nn_justine
    global nn_anthony
    global nn_combined
<<<<<<< HEAD
    global count
    if count % 500 == 0:
        allow_things = []
        with open('connection.txt', 'r') as fs:
            allow_things = [i.strip() for i in fs.readlines()]
        ID_JUSTINE = False
        ID_ANTHONY = False
        ID_FIRE = False
        if 'justine' in allow_things:
            ID_JUSTINE = True
        if 'anthony' in allow_things:
            ID_ANTHONY = True
        if 'fire' in allow_things:
            ID_FIRE = True
    count += 1
=======

>>>>>>> bee59e5... much more stuff than you should have in one commit
    data = np.fromstring(in_data, 'Float32')
    # print(len(data))

    # data has NaNs in it; filter them out
    data_i = np.arange(len(data))
    mask = np.isfinite(data)
    filtered_data = np.interp(data_i, data_i[mask], data[mask])

    fft_data = np.fft.fft(filtered_data)
    real_fft = np.absolute(fft_data)
    real_fft /= np.max(np.abs(real_fft),axis=0)
    # print(real_fft)
    # categorization = nn_combined.predict(np.asarray([real_fft, real_fft])[0:1])[0]
    # is_null = 1 == categorization[0]
    # is_anthony = 1 == categorization[1]
    # is_justine = 1 == categorization[2]
    # is_fire = 1 == categorization[3]
    # if any(categorization):
    #     print 'is_anthony:', is_anthony, 'is_justine:', is_justine, 'is_fire:', is_fire
    # play = is_anthony
    # fire = nn_fire.predict_proba(np.asarray([real_fft, real_fft])[0:1])[0][1]
    # ant = [0] == 1
<<<<<<< HEAD
    # test = nn_fire.predict(np.asarray([real_fft, real_fft])[0:1])
    # print test
    # ant = test[0] == 1
=======
    sys.stdout = open(os.devnull, "w")
    test = nn_fire.predict(np.asarray([real_fft, real_fft])[0:1])
    sys.stdout = sys.__stdout__
    # print test
    ant = test[0] == 1
>>>>>>> bee59e5... much more stuff than you should have in one commit
    # if ant:
    #     print 'True'
    # just = nn_justine.predict_proba(np.asarray([real_fft, real_fft])[0:1])[0][1]
    # print 'fire', fire>0.8, 'ant', ant>0.8, 'just', just>0.8
<<<<<<< HEAD
    # play = ant
    sys.stdout = open(os.devnull, "w")
    play = ID_FIRE and 1 == nn_fire.predict(np.asarray([real_fft, real_fft])[0:1])[0]
    play = play or (ID_JUSTINE and 1 == nn_justine.predict(np.asarray([real_fft, real_fft])[0:1])[0])
    play = play or (ID_ANTHONY and 1 == nn_anthony.predict(np.asarray([real_fft, real_fft])[0:1])[0])
    sys.stdout = sys.__stdout__
=======
    play = ant
    # play = ID_FIRE and 1 == nn_fire.predict(np.asarray([real_fft, real_fft])[0:1])[0]
    # play = play or (ID_JUSTINE and 1 == nn_justine.predict(np.asarray([real_fft, real_fft])[0:1])[0])
    # play = play or (ID_ANTHONY and 1 == nn_anthony.predict(np.asarray([real_fft, real_fft])[0:1])[0])
>>>>>>> bee59e5... much more stuff than you should have in one commit
    # try:
    # print('before predict')
    # play =  or 1 == nn_justine.predict(np.asarray([real_fft, real_fft])[0:1])[0]
    # print('play', play)
    # except:
    #     pass
    if play:
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
    time.sleep(0.001)

stream.stop_stream()
stream.close()

p.terminate()
