import streamlit as st  # Import the Streamlit library

# Define a function to convert units based on predefined conversions factors or formulas
def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000, # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001, # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000, # 1 kilogram = 1000 grams
    }
    key = f"{unit_from}_{unit_to}" # generate a unique key for the conversion
    # logic to convert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        # return a message if the conversion is not Supported
        return "Conversion not Supported"
    
# Title of the app
st.title("Unit Converter")

# Create input fields for the user to enter the value and select the units to convert
value = st.number_input("Enter the value:", min_value = 1.0, step = 1.0)

# Dropdown to select the units to convert from
unit_from = st.selectbox("Convert From:", ["meters", "kilometers", "grams", "kilograms"])

# Dropdown to select the units to convert to
unit_to = st.selectbox("Convert To:", ["meters", "kilometers", "grams", "kilograms"])

# Button to perform the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # Call the convert_units function

    # Display the result
    st.write(f"{value} {unit_from}  =  {result} {unit_to}")