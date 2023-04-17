import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib
import streamlit as st
from streamlit_extras.stateful_button import button

st.title("CardioCare: Personalised Heart Disease Risk Assessment and Lifestyle Improvement App")
st.text('')
st.write("""CardioCare calculates a personalised heart disease risk score for you. \n
It is based on the personal data provided by you below. \n
After clicking the button below, you'll be asked to fill out a short survey. \n
Once completed, you'll be given a CVD likelihood score and recommendations \n
on lifestyle improvements based on your survey answers.""")
         
feature_names = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
    'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'PhysicalActivity',
    'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer', 'Race_Asian',
    'Race_Black', 'Race_Hispanic', 'Race_Other', 'Race_White',
    'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
    'GenHealth_Very good', 'Diabetic_No, borderline diabetes',
    'Diabetic_Yes', 'Diabetic_Yes (during pregnancy)']

if button("Take Control of Your Heart Health.", key='button1'):

    user_inputs = []
    AgeCategory = st.number_input('How old are you?', key=1, step =1)
    user_inputs.append(AgeCategory)

    height = st.number_input("What is your height in cm?", min_value = 1, key=2, step=1)
    weight =  st.number_input("What is your weight in kg?", min_value = 1, key=3, step=1)
    BMI = weight / (height/100)**2
    user_inputs.append(BMI)
    Sex = 1 if st.text_input("Are you Male or Female? Please answer 'Male' or 'Female'", key=4) == 'Male' else 0
    user_inputs.append(Sex)
    st.text('')
    st.write("Which race or ethnicity best describes you. (Please type 'Yes' into one of the options.)")
    st.text(' ')
    Race_Asian = 1 if st.text_input("Asian / Pacific Islander: ", value="No", key=5) == 'Yes' else 0
    user_inputs.append(Race_Asian)
    Race_Black = 1 if st.text_input("Black or African American: ", value="No", key=6) == 'Yes' else 0
    user_inputs.append(Race_Black)
    Race_Hispanic = 1 if st.text_input("Hispanic: ", value="No", key=7) == 'Yes' else 0 
    user_inputs.append(Race_Hispanic)
    Race_White = 1 if st.text_input("White / Caucasian: ", value="No", key=8) == 'Yes' else 0
    user_inputs.append(Race_White)
    Race_Other = 1 if st.text_input("Other Race or Ethnicity: ", value="No", key=9) == 'Yes' else 0
    user_inputs.append(Race_Other)

    st.text(' ')
    st.write("People present with diabetes in different ways. Which of the options apply to you?")
    st.write("If none apply to you, please move on to the next question")
    st.text(' ')
    Diabetic_Yes =  1 if st.text_input("I have been diagnosed with diabetes: ", value="No", key=10) == 'Yes' else 0
    user_inputs.append(Diabetic_Yes)
    Diabetic_No_borderline_diabetes = 1 if st.text_input("I have been diagnosed with borderline Type 2 diabetes: ", value="No", key=11) == 'Yes' else 0
    user_inputs.append(Diabetic_No_borderline_diabetes)
    Diabetic_Yes_during_pregnancy = 1 if st.text_input("I was diagnosed with diabetes during pregnancy: ", value="No", key=12) == 'Yes' else 0
    user_inputs.append(Diabetic_Yes_during_pregnancy)

    st.text(' ')
    st.write("How would you describe your general health?")
    st.text(' ')
    GenHealth_Poor =  1 if st.text_input("Poor: ", value="No", key=13) == 'Yes' else 0
    user_inputs.append(GenHealth_Poor)
    GenHealth_Fair =  1 if st.text_input("Fair: ", value="No", key=14) == 'Yes' else 0
    user_inputs.append(GenHealth_Fair)
    GenHealth_Good =  1 if st.text_input("Good: ", value="No", key=15) == 'Yes' else 0
    user_inputs.append(GenHealth_Good)
    GenHealth_Very_Good =  1 if st.text_input("Very Good: ", value="No", key=16) == 'Yes' else 0
    user_inputs.append(GenHealth_Very_Good)

    st.text(' ')
    st.write("Please answer 'Yes' or 'No' to the following questions:")
    st.text(' ')
    PhysicalActivity = 1 if st.text_input('Do you exercise outside of your regular job?', key=17, value = "No") == 'Yes' else 0
    user_inputs.append(PhysicalActivity)
    Smoking = 1 if st.text_input('Are you a smoker/do you smoke socially?', key=18, value = "No") == 'Yes' else 0
    user_inputs.append(Smoking)
    AlcoholDrinking = 1 if st.text_input('Depending on your sex (male/female), do you consume over 14/7 drinks per week (beer/wine)', key=19, value = "No") == 'Yes' else 0
    user_inputs.append(AlcoholDrinking)
    Stroke = 1 if st.text_input('Have you ever been diagnosed with a Stroke?', key=20, value = "No") == 'Yes' else 0
    user_inputs.append(Stroke)
    DiffWalking = 1 if st.text_input('Do you have serious difficulty walking or climbing stairs?', key=21, value = "No") == 'Yes' else 0
    user_inputs.append(DiffWalking)
    Asthma = 1 if st.text_input('Have you been diagnosed with Asthma?', key=22, value = "No") == 'Yes' else 0
    user_inputs.append(Asthma)
    KidneyDisease =  1 if st.text_input('Have you been diagnosed with Kidney Disease at any point in your life?', key=23, value = "No") == 'Yes' else 0
    user_inputs.append(KidneyDisease)
    SkinCancer = 1 if st.text_input('Have you been diagnosed with Skin Cancer at any point in your life?', key=24, value = "No") == 'Yes' else 0
    user_inputs.append(SkinCancer)
    st.text(' ')

    PhysicalHealth = st.number_input('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days).', key=25, step=1, max_value = 30, min_value = 0)
    user_inputs.append(PhysicalHealth)
    MentalHealth = st.number_input('Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days).', key=26, step=1, max_value = 30, min_value = 0)
    user_inputs.append(MentalHealth)
    SleepTime = st.number_input('On average, how many hours of sleep do you get in a 24-hour period (0-24)?', key=27, step=1, max_value = 30, min_value = 0)
    user_inputs.append(SleepTime)
    
    if button("Get your Heart Plan", key = 'button2'):
        
        user_input_order = [8, 0, 7, 14, 15, 16, 18, 17, 24, 23, 25, 21, 19, 20, 22, 9, 1, 2, 3, 6, 11, 12, 13, 4, 5, 10]
        if len(user_inputs) == len(feature_names):
            sort_indices = np.argsort(user_input_order)
            user_inputs = [user_inputs[i] for i in sort_indices]
            user_inputs_series = pd.Series(user_inputs, index=feature_names)
            user_data_df = pd.DataFrame(user_inputs_series).T
            model = joblib.load('./randund_version3_random_forest.pkl')
            y_predicted = model.predict_proba(user_data_df)
            st.subheader(f'Your likelihood of Heart Disease is {y_predicted[0, 1]*100:.2f}%')
        else:
            st.error("Error: Number of user inputs does not match number of features, please make sure you've answered all questions.")
        
        st.subheader("Your Lifestyle Plan: " )
        
        
        recommendations = []

        if user_data_df.loc[0, 'MentalHealth'] >= 5:
            st.write("""Although mental health won't directly affect your heart health, 
            keep in mind that a focus on improving your mental health will allow you to take effective action on any recommendations in your plan.""")
            st.write('Please find below the improvements you can make to your lifestyle in order of effectiveness:')
        else: 
            st.write('Please find below the improvements you can make to your lifestyle in order of effectiveness:')

        if user_data_df.loc[0, 'BMI'] < 17.5:
            recommendations.append('Your BMI is a little lower than it should be, try graining some weight through a combination of diet and exercise.')
        elif user_data_df.loc[0, 'BMI'] > 27.5:
            recommendations.append('Your BMI is a little higher than it should be, try losing some weight through a combination of diet and exercise.')
        else:
            pass

        if user_data_df.loc[0, 'Smoking'] == 1:
            recommendations.append('Quit smoking of all kinds. NHS Smokefree: This is a free service that provides support and advice on quitting smoking. You can get a free quit kit, sign up for a quit plan, and get support from trained advisors via phone, text, or online chat. https://www.nhs.uk/better-health/quit-smoking/')
        else:
            pass

        if user_data_df.loc[0, 'SleepTime'] < 5:
            recommendations.append('Try and improve your sleep time, heres a link to a website that can help you do this, https://www.nhs.uk/every-mind-matters/coronavirus/how-to-fall-asleep-faster-and-sleep-better/. Apps like Sleep Cycle can also help by tracking your sleep.') 
        else:
            pass

        if user_data_df.loc[0, 'PhysicalActivity'] == 0:
            recommendations.append('Find time to exercise outside of your regular job. The british heart foundation recommends people try and do atleast 30 minutes of exercise a day.')
        else:
            pass

        if user_data_df.loc[0, 'AlcoholDrinking'] == 0:
            if user_data_df.loc[0, 'Sex'] == 1:
                recommendations.append("""You're doing fantastically on most heart metrics. 
                                You might be interested to know that a small volume of alcohol each week can improve heart health. 
                                Generally having up to two small glasses of wine or two bottles of beer a day will improve the levels of 'good' cholesterol in your body.""")
            else:
                recommendations.append("""You're doing fantastically on most heart metrics. 
                        You might be interested to know that a small volume of alcohol each week can improve heart health. 
                        Generally having a small glass of wine or a bottle of beer a day will improve the levels of 'good' cholesterol in your body.""")   

        if recommendations == []:
             st.write("""You're ticking all the boxes and we can't currently recommend any lifestyle improvements. Keep it up! 
                        If you're still concerned about your score it may be due to health metrics outside of your immediate control. A healthcare professional can help you if this is the case.""")
        else:
            for i in range(len(recommendations)):
                st.write("Priority ",i+1, ": ")
                st.write(recommendations[i])



# If metric threshold passed, append output to a list, do this for each feature and print index 0 for best etc....