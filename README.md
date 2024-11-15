# Smart ATS: Resume Evaluation Tool

Smart ATS is a web-based application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). The app analyzes your resume against a provided job description, evaluating keyword matches, skills relevance, and areas for improvement. It uses advanced AI (Gemini) to provide insights that can enhance the chances of getting noticed by hiring systems and recruiters.

## Features

- **ATS Resume Evaluation**: Analyze your resume based on the job description to receive match percentages, missing skills, and other useful insights.
- **Skill Match Analysis**: Get detailed insights into the match percentage for specific skills, helping you understand where your resume needs to be enhanced.
- **Profile Summary**: A summary of the candidate’s profile and suggestions for improvement.
- **Missing Keywords**: A list of important keywords missing from your resume that could improve the chances of passing ATS filters.
- **Areas to Improve**: Specific areas of your resume that require enhancement to align with the job description.

## Technologies Used

- **Streamlit**: For building the user interface.
- **Google Gemini AI**: For generating detailed insights and evaluations on the resume.
- **PyPDF2**: For reading and extracting text from PDF resumes.
- **dotenv**: For securely handling API keys and environment variables.
- **JSON**: For parsing and handling response data in a structured format.

   ![image](https://github.com/user-attachments/assets/4772e9d1-6606-42a1-aa6f-9cfb7feac98d)

## Usage

### 1. Upload a Resume:
- Upload your resume in PDF format using the file upload interface.
- Paste the relevant **Job Description** into the provided text area.

 ![Screenshot 2024-11-15 143307](https://github.com/user-attachments/assets/4ab4e406-110b-405a-aae3-94a398cc4932)

  
![image](https://github.com/user-attachments/assets/4772e9d1-6606-42a1-aa6f-9cfb7feac98d)

  
### 2. Submit for Evaluation:
- Once you’ve provided both the job description and uploaded your resume, click the **Submit** button.
- The tool will process your inputs and return a detailed ATS analysis, including overall match percentage, missing skills, and areas to improve.

  ![Screenshot 2024-11-15 143247](https://github.com/user-attachments/assets/cb5ec9d8-80d7-4cff-8511-32ceebed2ba9)

  

### 3. Interpret the Results:
- View the match percentage and specific feedback in a user-friendly format.
- Use the suggestions to improve your resume and increase the likelihood of getting past ATS filters.

  ![Screenshot 2024-11-15 143320](https://github.com/user-attachments/assets/832518c3-e3cc-45fd-847b-c938339d644c)

