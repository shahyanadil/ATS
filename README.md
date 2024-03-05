# Inhouse ATS

This Streamlit application serves as an in-house Applicant Tracking System (ATS), leveraging Google's Generative AI to evaluate resumes against given job descriptions. It provides insights into the relevance of the resume to the job requirements, suggests improvements, and assigns a percentage match based on the provided job description.

## Features:
- **Resume Evaluation:** Upload your resume in PDF format to evaluate its relevance to a given job description.
- **Job Description:** Enter the job description against which the resume will be evaluated.
- **AI Assistance:** Utilizes Google's Generative AI to analyze the resume and provide feedback.

## How to Use:
1. Enter the job description into the text area provided.
2. Upload your resume in PDF format using the file uploader.
3. Click the "Submit" button to initiate the evaluation process.
4. The application will display insights and feedback on the resume's relevance to the job description.

## Code Details:
- The application is built using Streamlit, a Python framework for building interactive web applications.
- It utilizes the `google.generativeai` library to access Google's Generative AI capabilities.
- Resumes are processed using the PyPDF2 library to extract text from PDF files.

## Prerequisites:
- Python installed on your system.
- Required Python libraries installed (`streamlit`, `PyPDF2`, `python-dotenv`).

## Installation:
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/<username>/<repository-name>.git
