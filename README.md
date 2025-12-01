# Customer Purchase Frequency Predictor

A Streamlit web application for predicting customer purchase frequency using a trained CatBoost classifier.

## Features

- 🛍️ Interactive web interface for making predictions
- 📊 Real-time probability visualization
- 📈 Confidence score display
- 🔮 Easy-to-use input controls (dropdowns and sliders)

## Installation

1. **Clone or download the project:**

```bash
cd "d:\Coding\Python\Personal Projects\ConsumerBehavior"
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Running the App

### Local Development

```bash
streamlit run app.py
```

This will open the app in your default browser at `http://localhost:8501`

### Deploy to Streamlit Cloud

1. **Push your code to GitHub:**

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Create a new app:**
   - Click "New app"
   - Select your GitHub repository
   - Select the branch (main)
   - Set the main file path to `app.py`
   - Click "Deploy"

### Deploy to Heroku

1. **Create a Procfile:**

```
web: streamlit run app.py
```

2. **Create a setup.sh file:**

```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = \$PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. **Deploy:**

```bash
heroku login
heroku create your-app-name
git push heroku main
```

## File Structure

```
ConsumerBehavior/
├── main.ipynb                      # Jupyter notebook with model training
├── app.py                          # Streamlit app
├── best_model.pkl                  # Trained model (pickle file)
├── shopping_behavior_updated.csv   # Dataset
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## How to Use

1. Open the app in your browser
2. Use the sidebar to input customer data:
   - Select categorical features from dropdowns
   - Adjust numerical features using sliders
3. Click "Predict Purchase Frequency"
4. View the prediction, confidence score, and probability breakdown

## Model Information

- **Algorithm:** CatBoost Classifier
- **Classes:** Annual, Bi-weekly, Monthly, Quarterly, Weekly
- **Input Features:** Age, Gender, Category, Location, Season, etc.
- **Cross-validation Score:** Available in training notebook

## Requirements

- Python 3.7+
- streamlit
- pandas
- numpy
- scikit-learn
- catboost
- matplotlib
- seaborn

## Troubleshooting

**Model not found error:**

- Ensure `best_model.pkl` exists in the same directory as `app.py`
- Run the Jupyter notebook to regenerate the model

**Port already in use:**

```bash
streamlit run app.py --server.port 8502
```

**Module not found:**

```bash
pip install -r requirements.txt
```

## Future Enhancements

- Add batch prediction from CSV files
- Include model performance metrics
- Add data visualization dashboard
- Implement API endpoint for model predictions
- Add user authentication

## License

This project is open source and available under the MIT License.
