import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Purchase Frequency Predictor", layout="wide")

# Title
st.title("🛍️ Customer Purchase Frequency Predictor")
st.markdown("---")

# Load the model
@st.cache_resource
def load_model():
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Load the training data to get feature info
@st.cache_resource
def load_data():
    df = pd.read_csv('./shopping_behavior_updated.csv')
    return df

try:
    model = load_model()
    df = load_data()
    
    # Get categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    categorical_cols.remove('Frequency of Purchases')
    
    # Get all feature columns (excluding target and ID)
    feature_cols = df.drop(['Frequency of Purchases', 'Customer ID'], axis=1).columns.tolist()
    
    st.success("✓ Model loaded successfully!")
    
    # Sidebar for input
    st.sidebar.header("📊 Input Customer Data")
    
    # Create input fields
    input_data = {}
    
    for col in feature_cols:
        if col in categorical_cols:
            # Get unique values for categorical columns
            unique_vals = sorted(df[col].unique())
            input_data[col] = st.sidebar.selectbox(f"Select {col}", unique_vals)
        else:
            # For numerical columns, get min and max from data
            min_val = int(df[col].min())
            max_val = int(df[col].max())
            input_data[col] = st.sidebar.slider(f"Select {col}", min_val, max_val, (min_val + max_val) // 2)
    
    # Create prediction button
    if st.sidebar.button("🔮 Predict Purchase Frequency", key="predict_btn"):
        # Prepare data for prediction
        input_df = pd.DataFrame([input_data])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]
        
        # Get class labels
        class_labels = sorted(df['Frequency of Purchases'].unique())
        
        # Display results
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📌 Prediction Result")
            st.metric("Predicted Frequency", str(prediction))
        
        with col2:
            st.subheader("📊 Confidence Score")
            highest_prob = max(probabilities) * 100
            st.metric("Confidence", f"{highest_prob:.2f}%")
        
        # Display probability breakdown
        st.subheader("📈 Prediction Probabilities")
        
        prob_data = []
        for label, prob in zip(class_labels, probabilities):
            percentage = prob * 100
            prob_data.append({
                'Frequency': label,
                'Probability': f"{percentage:.2f}%",
                'Score': prob
            })
        
        # Create a dataframe for better visualization
        prob_df = pd.DataFrame(prob_data)
        
        # Display as table
        st.table(prob_df[['Frequency', 'Probability']])
        
        # Display as bar chart
        st.bar_chart(prob_df.set_index('Frequency')['Score'])
        
        # Display input summary
        st.subheader("📋 Input Data Summary")
        st.write(input_df.T)
    
    # Info section
    st.markdown("---")
    with st.expander("ℹ️ About This App"):
        st.write("""
        This application uses a trained CatBoost classifier to predict customer purchase frequency
        based on their shopping behavior data.
        
        **Classes:**
        - Annual: Customer purchases once a year
        - Bi-weekly: Customer purchases every two weeks
        - Monthly: Customer purchases once a month
        - Quarterly: Customer purchases once every three months
        - Weekly: Customer purchases once a week
        
        **How to use:**
        1. Enter customer data in the sidebar
        2. Click the "Predict Purchase Frequency" button
        3. View the prediction and confidence scores
        """)

except FileNotFoundError:
    st.error("❌ Error: Model file 'best_model.pkl' not found. Please save the model first.")
except Exception as e:
    st.error(f"❌ Error: {str(e)}")
