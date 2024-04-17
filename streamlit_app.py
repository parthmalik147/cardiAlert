import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="cardiAlert",
                   layout="wide",
                   page_icon=":heart:")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

#diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

#parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',

                           ['About us',
                            'Heart Disease Prediction',
                            'Explore'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# About us Page
if selected == 'About us':

    # page title
    st.title('cardiAlert')
    st.write('''
    ### cardiAlert is a web application which assits healthcare professionals to assess the risk of heart disease. It takes in the clinical data of the patient and makes informed decisions using machine learning. This application is intended to be used by professionals.
    ##      This web-app is developed by a team of students of GD Goenka University as their Design-Thinking project.
    ''')
    

    
    post ={
            
            "image_url": "team.jpg",
        }
    st.image(post['image_url'], use_column_width=True)
    st.markdown("<h5 style='text-align: center; color: grey;'>team cardiAlert</h5>", unsafe_allow_html=True)

    st.write('''
    ### streamlit app and the ML model is heavily inspired by siddhardhan23 at GitHub.
    ### Do check his work out at 
    ##### https://github.com/siddhardhan23/multiple-disease-prediction-streamlit-app
    ''')

       

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    st.write("Note: This application is designed to be used by a trained healthcare professional as it requires the knowledge and possession of technical clinical data of the patient. This is merely a tool to assist doctors and the predictions made by it should not be considered test results of any kind.")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex (0: female  1: male )')

    with col3:
        cp = st.text_input('Chest Pain (scale: 0 - 4)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm/Hg)')

    with col2:
        chol = st.text_input('Serum Cholestoral (mg/dl)')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0: low  1: high)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (bpm)')

    with col3:
        exang = st.text_input('Exercise Induced Angina (0: no  1: yes)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (0 - 3.5)')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0, 1, 2)')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0, 1, 2)')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is at high risk of heart disease'
        else:
            heart_diagnosis = f'### The person is at a low risk of heart disease'

    st.success(heart_diagnosis)

#Explore Page
if selected == "Explore":

    # page title
    st.title("Explore")
    # Define your posts (you can fetch these from a database or API)
    posts = [
        {
            "author": "Binod -",
            "content": "Major reasons for heart diseases in India.",
            "image_url": "h1.jpg",
        },
        {
            "author": "Bhupendra Jogi -",
            "content": "How to live past 100!. Start a healthy life today.",
            "image_url": "h2.jpg",
        },
        {
            "author": "Siddhant Snake -",
            "content": "Types of Heart diseases. And what to do to prevent them",
            "image_url": "h3.jpg",
        },
        {
            "author": "iShowSpeed -",
            "content": "Looking for a doctor? see no furthur. DOCTORS NEAR YOU!",
            "image_url": "h4.jpg",
        },
    ]

    # Render each post
    for post in posts:
        st.write(f"## {post['author']}")
        st.write(f"### {post['content']}")
        st.image(post['image_url'], caption=post['content'], use_column_width=True)

    #st.markdown('<h4 class="slide-in-left">End of page</h4>', unsafe_allow_html=True)

    
