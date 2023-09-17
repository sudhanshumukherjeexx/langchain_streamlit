#! C:\Users\Asus\00 - Personal\langchain_streamlit\myenv\Scripts\python.exe

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

st.header('BRAND WIZARD', divider='rainbow')
#-----------------------------
#DISPLAY IMAGES AND TITLES
#-----------------------------
st.image("gamified.png", output_format="auto")


#-----------------------------
# TOOL DESCRIPTION
#-----------------------------
st.text("Are you starting a new business or looking to rebrand your existing venture?\nIntroducing BrandWizard, your trusted companion in the world of brand identity. \nBrandWizard is a cutting-edge AI-powered tool designed to effortlessly conjure \ncaptivating and memorable company names tailored to your unique vision and needs.")

st.divider()

#-----------------------------
# TOOL OPTIONS
#-----------------------------

#create industry selectbox
options_1 = ["Technology", "Healthcare", "Finance", "Retail", "Entertainment", "Education", "Other(Please Specify)"]
selection_1 = st.selectbox("What is the industry or sector that the company operates in? (Select all that apply...)", options=options_1)
#Text input for user entry
if selection_1 == "Other(Please Specify)":
    otherOption1 = st.text_input("Please specify your industry...")

st.divider()

#-------------------------------------------------------------------------------------------------------------------------------------------------------

#products and services
options_2 = ["Software", "Hardware", "Consulting", "E-commerce", "Manufacturing", "Financial Services", "Other(Please Specify)"]
selection_2 = st.selectbox("What are the main products or services offered by the company?", options=options_2)
#Text input for user entry
if selection_2 == "Other(Please Specify)":
    otherOption2 = st.text_input("Please specify your industry...")

st.divider()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Target Audience or Customer Base of the Company
options_3 = ["B2B (Business-to-Business)", "B2C (Business-to-Consumer)" ,"Both"]
selection_3 = st.selectbox("Who is the target audience or customer base of the company?", options=options_3)
#Text input for user entry
if selection_3 == "Both":
    selection_3 = "B2B (Business-to-Business) and B2C (Business-to-Consumer)"

st.divider()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Brand Image or Values
options_4 = ["Innovative", "Reliable", "Progressive", "Trustworthy", "Dynamic", "Creative"]
selection_4 = st.selectbox("What brand values or brand image do you want the name to convey? (Select all that apply...)", options=options_4)

st.divider()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Specific Keywords or themes 
options_5 = ["Technology", "Growth", "Solutions", "Global", "Future", "Harmony", "None"]
selection_5 = st.selectbox("Are there any specific keywords or themes that should be incorporated into the name? (Select all that apply...)", options=options_5)
if selection_5 == "None":
    selection_5 = "No Specific Words"

st.divider()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Length or Style of the Name
options_6 = ["Short and Catchy", "Modern and Trendy", "Descriptive and Informative", "Unique and Memorable"]
selection_6 = st.selectbox("Do you have any preferences in terms of the length or style of the name? (Select all that apply...)", options=options_6)

st.divider()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#LOAD ENVIRONMENT VARIABLES
load_dotenv(find_dotenv())

# -----------------------------------------
# PROMPT TEMPLATES: Manage Prompts for LLMs
# -----------------------------------------
# --------------------------------------------------------
# Chains: Combine LLMs and prompts in multi-step workflows
# --------------------------------------------------------


# -----------------------------------------
# BUTTON FUNCTIONALITIES & STATE
# -----------------------------------------


def generate_names():
    llm = OpenAI(model="text-davinci-003")
    prompt = PromptTemplate(
        input_variables=["industry", "products_or_services", "target_audience", "brand_values_image", "specific_keywords" ,"name_length_style_preference"],
        template="Suggest 10 names for a {industry} company offereing {products_or_services} to {target_audience} with a brand value or brand image of {brand_values_image}.I want {specific_keywords} words incorporated into the name. Please make sure the name is {name_length_style_preference}.",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(industry=selection_1, products_or_services=selection_2, target_audience=selection_3, brand_values_image=selection_4,specific_keywords=selection_5 ,name_length_style_preference=selection_6)
    return result

result_button = st.button("Generate Names")
if result_button:
    st.write(generate_names())


#****************************************************************************************