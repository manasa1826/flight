import streamlit as st
import joblib  # Use joblib instead of pickle

# Load the saved model
model_path = 'saved_models/flight_model.sav'
flight_model = joblib.load(model_path)  # Use joblib to load the model

# Page title
st.title('Flight Price Prediction')

# Mapping dictionaries for categorical data
airline_mapping = {'AirAsia': 1, 'Air_India': 2, 'GO_FIRST': 3, 'Indigo': 4, 'SpiceJet': 5, 'Vistara': 6}
city_mapping = {'Delhi': 1, 'Mumbai': 2, 'Bangalore': 3, 'Kolkata': 4, 'Hyderabad': 5, 'Chennai': 6}
time_mapping = {'Early_Morning': 1, 'Morning': 2, 'Afternoon': 3, 'Evening': 4, 'Night': 5, 'Late_Night': 6}
stops_mapping = {'zero': 0, 'one': 1, 'two_or_more': 3}
class_mapping = {'Economy': 1, 'Business': 2}

# Input fields for user data
col1, col2, col3 = st.columns(3)

with col1:
    airline = st.selectbox('Airline', list(airline_mapping.keys()))
    airline = airline_mapping[airline]

with col2:
    source_city = st.selectbox('Source City', list(city_mapping.keys()))
    source_city = city_mapping[source_city]

with col3:
    departure_time = st.selectbox('Departure Time', list(time_mapping.keys()))
    departure_time = time_mapping[departure_time]

with col1:
    stops = st.selectbox('Stops', list(stops_mapping.keys()))
    stops = stops_mapping[stops]

with col2:
    arrival_time = st.selectbox('Arrival Time', list(time_mapping.keys()))
    arrival_time = time_mapping[arrival_time]

with col3:
    destination_city = st.selectbox('Destination City', list(city_mapping.keys()))
    destination_city = city_mapping[destination_city]

with col1:
    flight_class = st.selectbox('Class', list(class_mapping.keys()))
    flight_class = class_mapping[flight_class]

with col2:
    duration = st.text_input('Duration (in hours)', '')

# Button for prediction
if st.button('Predict Flight Price'):
    # Ensure duration is a valid float
    try:
        duration = float(duration)
    except ValueError:
        st.error("Please enter a valid numerical value for duration.")
        st.stop()
    
    # Prepare the input data
    user_input = [airline, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration]
    
    # Predict the flight price
    price_prediction = flight_model.predict([user_input])
    
    # Display the predicted price
    st.success(f"The predicted price of the flight is ₹{price_prediction[0]:,.2f}")
