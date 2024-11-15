import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables (API key for Gemini)
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response based on input prompt
def get_gemini_response(input_prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text

# Function to extract text from uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Streamlit UI
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

# Job Description input
jd = st.text_area("Paste the Job Description")

# Resume PDF upload
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

# Submit button
submit = st.button("Submit")

# Process and generate response if 'Submit' button is pressed
if submit:
    if uploaded_file is not None and jd.strip() != "":
        # Extract text from the uploaded resume PDF
        resume_text = input_pdf_text(uploaded_file)

        # Replace placeholders in the prompt with actual data (resume text and job description)
        input_prompt = f"""
        Hey Act Like a skilled or very experienced ATS (Application Tracking System)
        with a deep understanding of the tech field, software engineering, data science, data analysis,
        and big data engineering. Your task is to evaluate the resume based on the given job description.
        You must consider the job market is very competitive and you should provide the best assistance 
        for improving the resumes. Assign the percentage matching based on JD and 
        the missing keywords with high accuracy.
        resume: {resume_text}
        description: {jd}

        I want the response in one single string having the structure:

        {{
          "Overall Match Percentage": "%",
          "Missing Skills Percentage": "%",
          "Profile Summary": "",
          "Skills Analysis": [
            {{
              "Skill": "Skill1",
              "Match Percentage": "X%",
              "Match Status": "Matched" / "Missing"
            }},
            {{
              "Skill": "Skill2",
              "Match Percentage": "Y%",
              "Match Status": "Matched" / "Missing"
            }},
            {{
              "Skill": "Skill3",
              "Match Percentage": "Z%",
              "Match Status": "Matched" / "Missing"
            }}
          ],
          "Missing Keywords": ["Keyword1", "Keyword2", "Keyword3"],
          "Areas to Improve": ["Area1", "Area2", "Area3"]
        }}
        """

        # Get the AI response
        response = get_gemini_response(input_prompt)

        # Parse and display the result in a more user-friendly format
        try:
            # Attempt to parse the response as JSON
            parsed_response = json.loads(response)
            st.subheader("ATS Resume Analysis")
            st.write(f"**Overall Match Percentage**: {parsed_response.get('Overall Match Percentage', 'N/A')}")
            st.write(f"**Missing Skills Percentage**: {parsed_response.get('Missing Skills Percentage', 'N/A')}")
            st.write(f"**Profile Summary**: {parsed_response.get('Profile Summary', 'N/A')}")
            st.write("### Skills Analysis")
            for skill in parsed_response.get("Skills Analysis", []):
                st.write(f"- **{skill['Skill']}**: {skill['Match Percentage']} ({skill['Match Status']})")
            st.write(f"**Missing Keywords**: {parsed_response.get('Missing Keywords', [])}")
            st.write(f"**Areas to Improve**: {parsed_response.get('Areas to Improve', [])}")
        except json.JSONDecodeError:
            # Handle if the response is not valid JSON
            st.error("Error parsing response. Please try again.")
    else:
        st.error("Please provide both a job description and upload a resume.")
