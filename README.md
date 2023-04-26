### <center> CAPSTONE PROJECT
### <center> Ollie Leach | OliverLeach95@gmail.com
### <center> https://github.com/OllieLeach95

# Title: CardioCare: Personalised Heart Disease Risk Assessment and Lifestyle Improvement Plan.
# TLDR: For those of you who dont have time to read through an entire repository, I've  recorded a quick 3 minute video that covers the project at a high level. https://www.loom.com/share/d13676c6cdda48749917d3c777b8d5f7

Cardiovascular disease (CVD) is the leading cause of death worldwide. In the USA alone, CVD is estimated to cost $555 billion per year, but early intervention is proven to reduce the financial burden. For every $1 spent on preventive measures an estimated $7 can be saved in the long run. 

Given these statistics, it seems sensible to create an app that acts as a preventative measure and empowers the general public to take control of their heart health. 

CardioCare is a machine learning aided app that aims to predict an individual's risk of developing CVD based on their personal data and provides users with a detailed report outlining their primary risk factors and personalized recommendations to improve their lifestyle.


Documents in this project folder (excluding this README and the Licensing agreement) include:

Reports and Summary Docs:
1. Oliver_Leach_Capstone_Final_Report.pdf - Summary of the process and results of the project
2. Oliver_Leach_Capstone_Final_Presentation.pdf - Capstone slide deck to be presented to class

models:
1. Model_download_instructions.pdf - Contains instructions for downloading the pkl files required to run the notebooks associated with this project.

notebooks:
1. Data_First_Look_and_EDA.ipynb - Cleaning and EDA of the dataset.
2. baseline_model.ipynb 
3. Modeling_Optimisation_and_Evaluation.ipynb

src/data:
1. Lifestyle_heart_data_clean.csv
2. Lifestyle_heart_data.csv

Visualisations:
1. Logistic_regression_equation.png
2. tree.dot - Extracted tree from final randomforest model
3. tree.png - Tree.dot converted to png

Streamlit:
1. capstonescript.py - Python file to run the streamlit app.
2. randund_version3_random_forest.pkl - Model referenced in the script.


Requirements:
1. capstone_env.yml - yml file containing the list of packages and their version numbers for the project environment
2. create_env_yml.sh - a shell script that allows for creation of a project environment when fed a .yml file.


