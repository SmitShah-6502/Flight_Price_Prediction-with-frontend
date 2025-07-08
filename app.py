from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

model = joblib.load('rf_flight_price_model.pkl')

# Recreate encoders using training classes
airline_encoder = LabelEncoder()
airline_encoder.classes_ = np.array(['Air Asia', 'Air India', 'Goair', 'IndiGo', 'Jet Airways', 'SpiceJet', 'Vistara'])

source_encoder = LabelEncoder()
source_encoder.classes_ = np.array(['Banglore', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai'])

destination_encoder = LabelEncoder()
destination_encoder.classes_ = np.array(['Banglore', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata'])

additional_info_encoder = LabelEncoder()
additional_info_encoder.classes_ = np.array(['Business class', 'In-flight meal not included', 'No Info', 'No check-in baggage included'])

def safe_label_encode(encoder, value, default):
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        return encoder.transform([default])[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        airline = request.form['Airline'].strip().title()
        source = request.form['Source'].strip().title()
        destination = request.form['Destination'].strip().title()
        total_stops = int(request.form['Total_Stops'])
        additional_info = request.form['Additional_Info'].strip().title()
        journey_day = int(request.form['Journey_day'])
        journey_month = int(request.form['Journey_month'])

        # Encode inputs safely
        airline_enc = safe_label_encode(airline_encoder, airline, 'IndiGo')
        source_enc = safe_label_encode(source_encoder, source, 'Delhi')
        destination_enc = safe_label_encode(destination_encoder, destination, 'Cochin')
        additional_info_enc = safe_label_encode(additional_info_encoder, additional_info, 'No Info')

        # Final features (7 user + 6 dummy defaults)
        features = [
            airline_enc,
            source_enc,
            destination_enc,
            total_stops,
            additional_info_enc,
            journey_day,
            journey_month,
            0,  # dep_hour default
            0,  # dep_min default
            0,  # arrival_hour default
            0,  # arrival_min default
            1,  # duration_hour default
            0   # duration_min default
        ]

        prediction = model.predict([features])[0]
        return render_template('index.html', prediction_text=f"Predicted Flight Price: ₹{round(prediction, 2)}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)



