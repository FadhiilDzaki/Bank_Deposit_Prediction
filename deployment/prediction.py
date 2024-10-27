
# Import library
import pandas as pd 
import streamlit as st 
import pickle

# Load Model
with open('knn_best.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    # Title
    st.title('DEPOSIT PREDICTOR')

    # Pemisah
    st.write('___')

    # Image
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsvXILx1-ACgdvXyZuOoTI4KVya7ErIbs5fg&s')

    # Form
    with st.form(key='form parameter'):
        age = st.number_input("Age", min_value=18, max_value=95, value=35)
        job = st.selectbox("Job", ['admin.', 'technician', 'services', 'management', 'retired', 
                                'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 
                                'self-employed', 'student', 'unknown'])
        marital = st.selectbox("Marital Status", ['single', 'married', 'divorced'])
        education = st.selectbox("Education", ['unknown', 'primary', 'secondary', 'tertiary'])
        default = st.selectbox("Has Credit in Default?", ['no', 'yes'])
        balance = st.number_input("Balance", min_value=-5000, max_value=6500, value=1000)
        housing = st.selectbox("Has Housing Loan?", ['no', 'yes'])
        loan = st.selectbox("Has Personal Loan?", ['no', 'yes'])
        contact = st.selectbox("Contact Type", ['unknown', 'telephone', 'cellular'])
        day = st.number_input("Last Contact Day of Month", min_value=1, max_value=31, value=20)
        month = st.selectbox("Last Contact Month", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                                                    'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        duration = st.number_input("Contact Duration (seconds)", min_value=0, max_value=5000, value=100)
        campaign = st.number_input("Number of Contacts During Campaign", min_value=1, max_value=30, value=1)
        pdays = st.number_input("Days Passed Since Last Contact", min_value=-1, max_value=1000, value=-1)
        previous = st.number_input("Number of Contacts Before This Campaign", min_value=0, max_value=100, value=0)
        poutcome = st.selectbox("Outcome of Previous Campaign", ['unknown', 'other', 'failure', 'success'])

        submit = st.form_submit_button('Predict')

    # Create a dictionary of user input
    data = {
        'age': [age],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'balance': [balance],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'day': [day],
        'month': [month],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'poutcome': [poutcome],
    }

    # Convert to DataFrame
    data_inf = pd.DataFrame(data)

    # Calculate 'week' from 'day' based on the conditions
    def assign_week(day):
        if day <= 7:
            return 1
        elif day <= 14:
            return 2
        elif day <= 21:
            return 3
        elif 21 < day <= 31:
            return 4
        else:
            return pd.NA

    # Apply week assignment
    data_inf['week'] = data_inf['day'].apply(assign_week)

    # Show Data
    st.dataframe(data_inf)

    # Predict
    if submit:
        # Preprocess data_inf if needed before prediction
        pred = model.predict(data_inf)
        st.write(f'### Deposit? {"Yes" if pred[0] == 1 else "No"}')

if __name__ == '__main__':
    run()
