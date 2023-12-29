**Math Formula Extractor**
Overview
The Math Formula Extractor is a web application developed using Streamlit that allows users to upload images containing mathematical formulas. The application utilizes the Gemini API to analyze the uploaded images, extract mathematical formulas, and display them in LaTeX format on an HTML canvas within the website.

*Features*
Website Development:

Built using Streamlit for the frontend.
Responsive and user-friendly design.
Image Upload Feature:

Users can upload images with mathematical formulas.
Formula Analysis:

Utilizes the Gemini API to analyze uploaded images.
Extracts mathematical formulas from the images.
Displaying Formulas:

Converts extracted formulas into LaTeX format.
Displays formulas on an HTML canvas within the website.
Testing and Validation:

Handles different image formats and sizes.
Download Option:

Provides an option to download the converted LaTeX code.
How to Use
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/math-formula-extractor.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file and add your Gemini API key:

makefile
Copy code
GEMINI_API_KEY=your-api-key
Run the application:

bash
Copy code
streamlit run app.py
Visit http://localhost:8501 in your web browser to use the application.

Screenshots
Include screenshots or GIFs demonstrating the usage of the application.

Dependencies
Streamlit
OpenAI Gemini API
PIL (Pillow)
dotenv
License
This project is licensed under the MIT License.

Acknowledgments
Streamlit
OpenAI Gemini API
