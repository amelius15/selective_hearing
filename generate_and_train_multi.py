import numpy as np
import pickle
from sknn.mlp import Regressor, Classifier, Layer
import logging
logging.basicConfig()
# null_set = np.load("10000_44100_512_NULL.npy")

# positive_set_anthony = np.load("10000_44100_512_ANTHONY.npy")

# positive_set_justine = np.load("10000_44100_512_JUSTINE.npy")

# positive_set_fire = np.load("10000_44100_512_FIRE_ALARM.npy")

# index_null = 0

# index_pos_ant = 0

# index_pos_fire = 0

# index_pos_just = 0

# data_x = None

# data_y = None
# for i in xrange(min(len(null_set), len(positive_set_anthony))*4):
#     print("index:", i)
#     if i%4 == 0: #null
#         if data_x is not None:
#             data_x = np.vstack((data_x, null_set[index_null]))
#         else:
#             data_x = null_set[index_null]
#         index_null+=1
#     elif i%4 == 1: #anthony
#         if data_x is not None:
#             data_x = np.vstack((data_x, positive_set_anthony[index_pos_ant]))
#         else:
#             data_x = positive_set_anthony[index_pos_ant]
#         index_pos_ant+=1
#     elif i%4 == 2: # justine
#         if data_x is not None:
#             data_x = np.vstack((data_x, positive_set_justine[index_pos_just]))
#         else:
#             data_x = positive_set_justine[index_pos_just]
#         index_pos_just+=1
#     else: # fire
#         if data_x is not None:
#             data_x = np.vstack((data_x, positive_set_fire[index_pos_fire]))
#         else:
#             data_x = positive_set_fire[index_pos_fire]
#         index_pos_fire+=1
#     y_param = [0,0,0,0]
#     y_param[i%4] = 1
#     if data_y is not None:
#         data_y = np.vstack((data_y, y_param))
#     else:
#         data_y = y_param

# np.save("data_x_combined", data_x)
# np.save("data_y_combined", data_y)

data_x = np.load("data_x_combined.npy")[100:]
data_y = np.load("data_y_combined.npy")[100:]
print data_y
nn = Regressor(
    layers=[
        Layer("Sigmoid", units=512),
        Layer("Sigmoid")],
    learning_rate=0.0001,
    n_iter=40
    )
print("Generating Fit")
nn.fit(data_x, data_y)
print("Fit generated")
fs = open('nn_combined_reg.pkl', 'wb')
pickle.dump(nn, fs)
fs = open('nn_combined_reg.pkl', 'rb')
nn = pickle.load(fs)
n = 2590
for x in nn.predict(data_x[n:n+2000]):
    if np.count_nonzero(x):
        print 'nonzero', x
# print()
# print(data_y[n:n+2000])
# nn.score(data_x, data_y)
# fs.close()
# print("NN Pickled")
# pickle.save()