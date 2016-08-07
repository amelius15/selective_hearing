import numpy as np
import pickle
from sknn.mlp import Classifier, Layer
import logging
logging.basicConfig()

def my_callback(event, **variables):
    print(event)        # The name of the event, as shown in the list above.
    # print(variables)

def shuffle_in_unison_scary(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

null_set = np.load("10000_44100_512_NULL.npy")[100:]

anthony_set = np.load("10000_44100_512_ANTHONY.npy")[100:]

justine_set = np.load("10000_44100_512_JUSTINE.npy")[100:]

fire_set = np.load("10000_44100_512_FIRE_ALARM.npy")[100:]

index_null = 0

index_pos = 0

index_neg = 0

data_x = np.vstack((null_set, anthony_set, justine_set, fire_set))

nulls = np.zeros(len(null_set))[np.newaxis].T

ant = np.zeros(len(anthony_set))[np.newaxis].T

just = np.zeros(len(justine_set))[np.newaxis].T

fire = np.ones(len(fire_set))[np.newaxis].T

data_y = np.vstack((nulls, ant, just, fire))

print 'stacked'

shuffle_in_unison_scary(data_x, data_y)

print 'shuffled'

np.save("data_x_fire_a", data_x)
np.save("data_y_fire_a", data_y)

print 'saved'

data_x = np.load("data_x_fire_a.npy")[100:]
data_y = 1*np.load("data_y_fire_a.npy")[100:]
nn = Classifier(
    layers=[
        Layer("Sigmoid", units=512),
        Layer("Softmax")],
    learning_rate=0.01,
    n_iter=40,
    # callback=my_callback
    )
print("Generating Fit")
nn.fit(data_x, data_y)
print("Fit generated")
fs = open('nn_fire_a.pkl', 'wb')
pickle.dump(nn, fs)
fs = open('nn_fire_a.pkl', 'rb')
nn = pickle.load(fs)
n = 259
# print(nn.predict_proba(data_x[n:n+20]))
out = np.column_stack((nn.predict_proba(data_x[n:n+20]), nn.predict(data_x[n:n+20]), data_y[n:n+20]))
print(out)
# print(data_y[n:n+20])
# nn.score(data_x, data_y)
# fs.close()
# print("NN Pickled")
# pickle.save()