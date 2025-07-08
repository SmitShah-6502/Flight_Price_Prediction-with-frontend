Flight Price Prediction System

🌟 Features
✈️ Flight Price Prediction – Predicts ticket prices using a trained Random Forest model based on features like Airline, Total_Stops, and Journey_Month.
📊 Exploratory Data Analysis (EDA) – Visualizes price distribution, airline-wise averages, stop distribution, and monthly trends.
🖥️ Interactive Web Interface – A modern, responsive design using HTML, CSS, and Flask for real-time predictions.
🔧 Model Optimization – Includes hyperparameter tuning for Random Forest and XGBoost using GridSearchCV.
🚀 Tech Stack
Frontend: HTML, CSS
Backend: Flask, Python, Pandas
Machine Learning: Scikit-learn, XGBoost, Joblib
Dataset: Flight_Fare.csv – A dataset with 10,683 records including Airline, Date_of_Journey, Source, Destination, Total_Stops, Duration, Additional_Info, and Price.
📂 Project Structure
text

Collapse

Wrap

Copy
├── app.py              # Flask backend with API routes
├── templates/
│   └── index.html      # Frontend UI
├── Flight_Fare.csv     # Dataset with flight details and prices
├── flight_price_prediction.ipynb # Jupyter notebook with analysis and modeling
├── rf_flight_price_model.pkl    # Serialized Random Forest model
├── requirements.txt    # Python dependencies
└── README.md           # Project description
📦 Installation & Run Locally
1. Clone the Repository
bash

Collapse

Wrap

Run

Copy
git clone https://github.com/your-username/flight-price-prediction.git
cd flight-price-prediction
2. Create a Virtual Environment
bash

Collapse

Wrap

Run

Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash

Collapse

Wrap

Run

Copy
pip install -r requirements.txt
4. Prepare the Dataset and Model
Ensure Flight_Fare.csv is in the project directory.
Run flight_price_prediction.ipynb to train and save the model as rf_flight_price_model.pkl, or use the provided pre-trained model.
5. Run the Flask App
bash

Collapse

Wrap

Run

Copy
python app.py
Visit http://127.0.0.1:5000 in your browser to use the predictor.
How It Works
Flight Price Prediction: Users input flight details (e.g., Airline, Source, Destination, Total_Stops, Journey_Day, Journey_Month) via the web form. The app encodes inputs, adds dummy defaults for missing features, and uses the Random Forest model to predict the price.
EDA Visualizations: The notebook includes a histogram of price distribution (right-skewed, ₹3000-₹10,000 common), a bar plot of average price by Airline, a pie chart of Total_Stops distribution (e.g., 50-60% non-stop), and a line chart of average price by Journey_Month (e.g., higher in December).
Model Training: Trains multiple models, tunes hyperparameters, and selects the best model based on R² and MSE metrics.
📌 Future Enhancements
🌍 Add real-time flight data integration (e.g., from APIs).
📅 Include dynamic date range selection for Journey_Day and Journey_Month.
☁️ Deploy on a cloud platform like Heroku or Render.
🤝 Credits
Dataset: Flight_Fare.csv (source to be specified if applicable, e.g., Kaggle or a public repository).
Inspiration: xAI and tools like Grok for AI-driven projects.
📄 License
This project is open-source under the MIT License.
