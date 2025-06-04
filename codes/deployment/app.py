from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained model and feature columns
model = joblib.load("model/career_predictor_model1.pkl")
feature_columns = joblib.load("model/feature_columns1.pkl")

# Slider ranges for input features
slider_ranges = {
    "Computer Architecture": (0.0, 6.0, 0),
    "Programming Skills": (0.0, 6.0, 0),
    "Project Management": (0.0, 6.0, 0),
    "Communication skills": (0.0, 6.0, 0),
    "Openness": (0.0, 1.0, 0),
    "Conscientousness": (0.0, 1.0, 0),
    "Extraversion": (0.0, 1.0, 0),
    "Agreeableness": (0.0, 1.0, 0),
    "Emotional_Range": (0.0, 1.0, 0),
    "Conversation": (0.0, 1.0, 0),
    "Openness to Change": (0.0, 1.0, 0),
    "Hedonism": (0.0, 1.0, 0),
    "Self-enhancement": (0.00, 1.0, 0),
    "Self-transcendence": (0.00, 1.0, 0)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html', features=feature_columns, slider_ranges=slider_ranges)

@app.route('/api/predict', methods=['POST'])
def predict():
    # Get user input from form
    user_input = {}
    all_default = True
    for feature in feature_columns:
        value = request.form.get(feature)
        try:
            user_input[feature] = float(value) if value else 0.0
            # Check if any value is different from the default (initial) value
            default_value = slider_ranges[feature][2]
            if user_input[feature] != default_value:
                all_default = False
        except (ValueError, TypeError):
            user_input[feature] = 0.0

    # If all inputs are at default values, return no-input response
    if all_default:
        return jsonify({'no_input': True})

    # Create DataFrame for prediction
    input_df = pd.DataFrame([user_input])
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Return JSON response
    return jsonify({
        'prediction': prediction,
        'input_summary': input_df.to_dict(orient='records')[0]
    })

if __name__ == '__main__':
    app.run(debug=True)