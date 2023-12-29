**Math Formula Extractor**

This app extracts mathematical formulas from images using the Gemini-Pro-Vision AI model and converts them into LaTeX code.

**Features**

-Upload images containing mathematical formulas (JPEG, PNG, or JPG formats).
-Extract formulas using AI and display them in both text and LaTeX format.
-Download the extracted formulas as a LaTeX file for further use.


Technologies Used:

Streamlit

google.generativeai

Pillow (PIL)

dotenv


**Setup**

Clone this repository.

Create a .env file and add your Gemini API key:

GEMINI_API_KEY=YOUR_API_KEY_HERE


Install the required libraries:

```console
pip install -r requirements.txt
```


Run the application:

```console
streamlit run app.py
```


**Usage:**

1. Access the app in your web browser.
2. Upload an image containing mathematical formulas. 
3. The app will display the extracted formulas in text and LaTeX format.
4. Click "Download LaTeX File" to download the formulas.


**License**

MIT License: https://choosealicense.com/licenses/mit/


**Additional Notes**

1. Requires a Google AI API key for the Gemini-Pro-Vision model.
2. Use clear images with well-defined formulas for optimal performance.
