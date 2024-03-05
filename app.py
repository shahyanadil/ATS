import streamlit as st
import google.generativeai as genai
import os 
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv() # load all variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Gemini Pro response

def get_gemini_resp(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf2text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(0,len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

## prompt template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

st.title("Inhouse ATS:")
st.text("Imporve your score")
jd= st.text_area("Please provide the job description")
uploaded_file = st.file_uploader("upload your resume", type = "pdf", help= "only for pdf")
submit = st.button("submit")
if submit:
   if uploaded_file is not None:
       text= input_pdf2text(uploaded_file)
       response = get_gemini_resp(input_prompt)
       st.subheader(response)