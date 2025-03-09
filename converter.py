import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color:rgb(23, 7, 48);
        color: white;
    }
    .stApp {
        background:linear-gradient(135deg,rgb(163, 69, 85), #00FF00 );
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    } 
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
        font-family: 'Arial', sans-serif; 
       
    } 
    .stButton>button {
        background: linear-gradient(45deg, purple, darkgreen);
        color: white;
        border: 2px;
        padding: 10px 20px;
        font-size: 20px;
        cursor: pointer;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #808080);
        color: white;
    } 
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: black;
        padding: 30px;
        border-radius: 13px;
        margin-top: 2px;
        box-shadow: 0px 10px 30px rgba(255, 20, 147, 0.8);
    } 
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 15px;
        color: black;
    }
    .stSidebar {
        background: linear-gradient(135deg,rgb(173, 137, 143) 40%,rgb(136, 192, 136) 60%);
    </style>  
    """,
    unsafe_allow_html=True
)

# title & description
st.markdown("<h1>Unit Converter using Python & Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# sidebar
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Grams", "Kilograms", "Pounds"])
    with col2:
        to_unit = st.selectbox("To", ["Grams", "Kilograms", "Pounds"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# function
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 
        'Kilometers': 0.001, 
        'Centimeters': 100
    }
    
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Grams': 1000, 
        'Kilograms': 1, 
        'Pounds': 2.2046
    }

    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value  
    return value

# button
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)                         

st.markdown("<div class='footer'>Created by Malaika Emaan 💗</div>", unsafe_allow_html=True)
