import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model
model_path = 'LinearRegressionModel1.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Load the data from the CSV file
data = pd.read_csv('Cleaned_Car_data.csv')

# Extract unique values for the dropdowns
company_list = data['company'].unique().tolist()
model_dict = {company: data[data['company'] == company]['name'].unique().tolist() for company in company_list}
year_list = sorted(data['year'].unique().tolist())
fuel_list = data['fuel_type'].unique().tolist()

html_title = """
<div style="background-color: #D3D3D3; padding: 10px; border-radius: 100px; text-align: center;">
    <h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif;">
        Welcome to <span style="color: #9966CC;">SELL IT</span> ---> Car Price Predictor
    </h1>
</div>
"""
st.markdown(html_title, unsafe_allow_html=True)

# Select Company
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>"
            "Select Company:</h3>", unsafe_allow_html=True)
company = st.selectbox('', company_list)

# Select Car's Model
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Select Car's Model:</h3>", unsafe_allow_html=True)
model_name = st.selectbox('', model_dict[company])

# Select Year of Purchase
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Select Year of Purchase:</h3>", unsafe_allow_html=True)
year = st.selectbox('', year_list)

# Select Fuel Type
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Select Fuel Type:</h3>", unsafe_allow_html=True)
fuel_type = st.selectbox('', fuel_list)


# Enter Number of Kilometers Travelled
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Enter Number of Kilometers Travelled:</h3>", unsafe_allow_html=True)
kms_driven = st.number_input('', min_value=0, step=1)

# Predict Price
if st.button('Predict Price'):
    # Create a DataFrame with the input features
    input_data = pd.DataFrame({
        'company': [company],
        'name': [model_name],
        'year': [year],
        'fuel_type': [fuel_type],
        'kms_driven': [kms_driven]
    })

    try:
        price = model.predict(input_data)[0]
        st.success(f'The predicted price of the car is Rs{price:.2f}')
    except Exception as e:
        st.error(f"Error in prediction: {e}")

prompt = st.chat_input("Tell us your Experience")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
st.markdown("""
---
*Created by Kunikaa Dwivedi with ❤️ using [Streamlit](https://streamlit.io/)*
""")