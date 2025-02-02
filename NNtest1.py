import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import sparse_categorical_crossentropy

import matplotlib.pyplot as plt

#####################################
#######---Lettura dati---############
#####################################

train_wf_all = np.loadtxt('../../train_wf.csv',delimiter=',')
train_label_all = np.loadtxt('../../train_label.csv',delimiter=',')
print(train_wf_all.shape)
print(train_label_all.shape)

shuffler = np.random.permutation(len(train_label_all))
train_wf_all = train_wf_all[shuffler]
train_label_all = train_label_all[shuffler]

val_wf = train_wf_all[1800:]
val_label = train_label_all[1800:]
train_wf = train_wf_all[:1800]
train_label = train_label_all[:1800]

print(train_wf.shape)
print(train_label.shape)
print(val_wf.shape)
print(val_label.shape)

#####################################
#######---Rete neurale---############
#####################################
'''
lr_schedule = keras.optimizers.schedules.InverseTimeDecay(0.001,
														  decay_steps=200*2000,
														  decay_rate=1,
														  staircase=False)'''

mod = Sequential([Dense(units=16, input_shape=(5000,), activation='relu'),
				  #Dense(units=8, activation='relu'),
				  #Dense(units=8, activation='relu'),
				  #Dense(units=8, activation='relu'),
				  Dense(units=2, activation='softmax')
				  #Dense(units=2)
				  ])
'''
model1 = Sequential([
	Dense(units=16, input_shape=(5000,), activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
	#Dropout(0.5),
	Dense(units=8, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
	#Dense(units=16, activation='relu'),
	Dense(units=2, activation='softmax')
])'''

mod.compile(optimizer = Adam(),
			   loss='sparse_categorical_crossentropy',
			   metrics=['accuracy'])

hist = mod.fit(x=train_wf, y=train_label,
             	  validation_data = (val_wf, val_label),
				  epochs=20,
				  shuffle=True,
				  verbose=1)

mod.summary()

print(train_wf.shape)
print(train_label.shape)
print(val_wf.shape)
print(val_label.shape)

'''
acc = hist.history['accuracy']
val_acc = hist.history['val_accuracy']
loss = hist.history['loss']
val_loss = hist.history['val_loss']
epoch= range(1,401)

plt.plot(epoch, loss, label='loss')
plt.plot(epoch, val_loss, label='val_loss')
plt.legend()
plt.show()
'''
