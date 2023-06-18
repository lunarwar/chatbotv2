import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np

nltk.download("punkt")
nltk.download("wordnet")

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

def preprocess_input(input_text):
    tokenized_text = nltk.word_tokenize(input_text)
    tokenized_text = [lemmatizer.lemmatize(word.lower()) for word in tokenized_text]
    return tokenized_text

def preprocess_training_data(intents):
    words = []
    classes = []
    documents = []
    ignore_chars = ["?", "!", ".", ","]

    for intent in intents:
        for pattern in intent["patterns"]:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent["tag"]))
            if intent["tag"] not in classes:
                classes.append(intent["tag"])

    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_chars]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    training_data = []
    output_data = []
    output_empty = [0] * len(classes)

    for document in documents:
        bag = []
        word_patterns = document[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
        for word in words:
            bag.append(1) if word in word_patterns else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1

        training_data.append(bag)
        output_data.append(output_row)

    training_data = np.array(training_data)
    output_data = np.array(output_data)

    return training_data, output_data, words, classes