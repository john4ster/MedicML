# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
from neural_network import NeuralNetwork
import torch
import os

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app)

# Serve the static files from the React dist directory
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

# Load the pickled model
with open('pickle-files/nn-tfidf-model.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)

# Load the pickled tfidf vectorizer
with open('pickle-files/tfidf-vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Load the pickled label encoder
with open('pickle-files/label-encoder.pkl', 'rb') as encoder_file:
    label_encoder = pickle.load(encoder_file)

# Route to get prediction given symptom description and the number of predictions to return
@app.route('/get_predictions', methods=['POST'])
def get_prediction():
    # Get symptom description and number of predictions wanted from request
    symptom_description = request.json['symptomDescription']
    num_predictions = request.json['topN'] # Number of predictions to return

    # Preprocess the input data using the vectorizer
    symptoms_tfidf = vectorizer.transform([symptom_description])
    symptoms_tensor = torch.tensor(symptoms_tfidf.toarray(), dtype=torch.float32)
    
    # Make predictions
    with torch.no_grad():
        outputs = model(symptoms_tensor)
        
        # Get the top n predictions
        top_n_values, top_n_indices = torch.topk(outputs, num_predictions, dim=1)
    
    # Decode the predictions
    predicted_labels = label_encoder.inverse_transform(top_n_indices.numpy().flatten())
    
    # Calculate percentages
    top_n_percentages = torch.nn.functional.softmax(top_n_values, dim=1).numpy().flatten() * 100
    top_n_percentages = top_n_percentages.astype(float)
    
    # Prepare the response
    predictions = [{'label': label, 'percentage': percentage} for label, percentage in zip(predicted_labels, top_n_percentages)]
    
    # Return prediction
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)