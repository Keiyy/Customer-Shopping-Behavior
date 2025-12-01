# Customer Purchase Frequency Predictor

A Streamlit web application for predicting customer purchase frequency using a trained CatBoost classifier.

## Features

- 🛍️ Interactive web interface for making predictions
- 📊 Real-time probability visualization
- 📈 Confidence score display
- 🔮 Easy-to-use input controls (dropdowns and sliders)

## Installation

1. **Clone the repository:**

```powershell
git clone https://github.com/Keiyy/Customer-Shopping-Behavior.git
cd Customer-Shopping-Behavior
```

2. **(Optional) Create and activate a conda environment:**

```powershell
conda create -n tf python=3.8
conda activate tf
```

3. **Install dependencies:**

```powershell
pip install -r requirements.txt
```

## Running the App

```powershell
streamlit run app.py
```

This will open the app in your default browser at `http://localhost:8501`

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

**Module not found / 'streamlit' not recognized:**

- Make sure your conda environment is activated: `conda activate tf`
- Install missing packages: `pip install -r requirements.txt`

**Port already in use:**

```powershell
streamlit run app.py --server.port 8502
```

**Conda not working in PowerShell:**
If `conda` is not recognized, run:

```powershell
conda init powershell
```

Then restart PowerShell and activate your environment again.

## Future Enhancements

- Add batch prediction from CSV files
- Include model performance metrics
- Add data visualization dashboard
- Improve model accuracy with hyperparameter tuning

## License

This project is open source and available under the MIT License.
