import random
import pymysql
from utils.preprocessing import preprocess_input, preprocess_training_data
from utils.training import train_model
import numpy as np
import tensorflow as tf
import os
from dotenv import load_dotenv
load_dotenv()
# Connect to the MySQL database
db = pymysql.connect(
    host= os.getenv('host'),
    port=int(os.getenv('port')),
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database')
)

# Fetch intents data from the database
cursor = db.cursor()
cursor.execute("SELECT * FROM intents")
data = cursor.fetchall()

# Get column names from cursor description
column_names = [desc[0] for desc in cursor.description]

# Convert rows to a list of dictionaries
intents = []
for row in data:
    intent = dict(zip(column_names, row))
    intent["patterns"] = eval(intent["patterns"])
    intent["responses"] = eval(intent["responses"])
    intents.append(intent)

# Preprocess training data
training_data, output_data, words, classes = preprocess_training_data(intents)

# # Train the model (if needed)
# train_model(training_data, output_data, classes)

# Load the trained model
model = tf.keras.models.load_model("models/chatbot_model.h5")

# Function to generate a response
def generate_response(predicted_class):
    for intent in intents:
        if intent["tag"] == predicted_class:
            response = random.choice(intent["responses"])
            break
    else:
        response = "Sorry, I didn't understand. Can you please rephrase?"

    return response
def place_holder_init():
    return "Job completed fine"
# ##Main interaction loop
# while True:
#     user_input = input("You: ")/
#     preprocessed_input = preprocess_input(user_input)
#     bag = [0] * len(words)
#     for word in preprocessed_input:
#         for i, w in enumerate(words):
#             if w == word:
#                 bag[i] = 1

#     results = model.predict(np.array([bag]))[0]
#     predicted_class_index = np.argmax(results)
#     confidence = results[predicted_class_index]

#     if confidence > 0.6:
#         predicted_class = classes[predicted_class_index]
#     else:
#         predicted_class = "unknown"

#     response = generate_response(predicted_class)
#     print("Bot:", response)
#     if predicted_class == "goodbye":
#         break

# Close the database connection
print(place_holder_init())
print("testing git control triggers")
db.close()