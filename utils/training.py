import tensorflow as tf
from tensorflow.keras import layers
# import os


# root_dir = os.path.dirname(os.path.abspath(__file__))
    
def train_model(training_data, output_data, classes):
    model = tf.keras.Sequential()
    model.add(layers.Dense(128, input_shape=(len(training_data[0]),), activation="relu"))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(len(output_data[0]), activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    history = model.fit(training_data, output_data, epochs=100, batch_size=8)

    # file_path = os.path.join(root_dir, 'models', 'chatbot_model.h5')
    model.save('models/chatbot_model.h5')