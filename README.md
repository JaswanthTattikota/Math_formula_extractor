 # **Math Formula Extractor**

This app extracts mathematical formulae from images using the Gemini-Pro-Vision AI model and converts them into LaTeX code. The LaTeX code can then be downloaded by clicking the <b>Download LaTeX File</b> button.  

 ## **Features**

-Upload images containing mathematical formulas (JPEG, PNG, or JPG formats).

-Extract formulas using AI and display them in both text and LaTeX format.

-Download the extracted formulas as a LaTeX file for further use.


## Technologies Used:

1. Streamlit
2. google.generativeai
3. Pillow (PIL)
4. dotenv


## **Setup**

Clone this repository by using the command:

```console
git clone https://github.com/JaswanthTattikota/Math_formula_extractor.git
```

After cloning the repository, change to the cloned repository's directory by using the following command:

```console
cd Math_formula_extractor
```

Create a .env file and add your Gemini API key:

```console
GEMINI_API_KEY = YOUR_API_KEY_HERE
```

Install the required libraries:

```console
pip install -r requirements.txt
```


Run the application:

```console
streamlit run app.py
```


## **Usage:**

1. Access the app in your web browser.
2. Upload an image containing mathematical formulas. 
3. The app will display the extracted formulas in text and LaTeX format.
4. Click "Download LaTeX File" to download the formulas.


### **License:**

MIT License

Copyright (c) [2023] [Jaswanth]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


### **Additional Notes:**

1. Requires a Google AI API key for the Gemini-Pro-Vision model.
2. Use clear images with well-defined formulas for optimal performance.
