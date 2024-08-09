# app.py
from flask import Flask, request, jsonify
import pickle
from neural_network import NeuralNetwork
import torch

app = Flask(__name__)

# Load the pickled model
with open('pickle-files/nn-tfidf-model.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)

# Load the pickled tfidf vectorizer
with open('pickle-files/tfidf-vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Load the pickled label encoder
with open('pickle-files/label-encoder.pkl', 'rb') as encoder_file:
    label_encoder_train = pickle.load(encoder_file)

@app.route('/')
def home():
    return "Welcome to the MedicalAssist API"

# Route to get prediction given symptom description
@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    # Get symptom description from request
    symptom_description = request.json['symptom_description']
    
    # Preprocess the input data using the vectorizer
    symptoms_tfidf = vectorizer.transform([symptom_description])
    symptoms_tensor = torch.tensor(symptoms_tfidf.toarray(), dtype=torch.float32)
    
    # Make predictions
    with torch.no_grad():
        outputs = model(symptoms_tensor)
        _, predicted = torch.max(outputs, 1)
    
    # Decode the predictions
    predicted_labels = label_encoder_train.inverse_transform(predicted.numpy())
    print(predicted_labels)
    
    # Return prediction
    return jsonify({'prediction': predicted_labels[0]})

if __name__ == '__main__':
    app.run(debug=True)