from _04_cnn_training_3 import *

import tensorflow as tf

model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(24,(5,5),strides=(2,2),padding="same",
        activation='relu',input_shape=x_train.shape[1:]),
    tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Conv2D(32,(5,5),strides=(2,2),padding="same",
        activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Conv2D(64,(5,5),strides=(2,2),padding="same",
        activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Conv2D(64,(3,3),padding="same",activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(100,activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(50,activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(4,activation='softmax')
])
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',metrics=['accuracy'])

history=model.fit(x_train,y_train,epochs=50,
                  validation_data=(x_valid,y_valid))
loss=history.history['loss']

epochs=range(1,len(loss)+1)

import matplotlib.pyplot as plt

plt.plot(epochs,loss,'g',label='Training loss')
plt.title('Training loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


model.save("model.keras")