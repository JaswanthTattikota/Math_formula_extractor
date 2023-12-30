import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

st.set_page_config(
    page_title="Math Formula Extractor",
    page_icon="https://seeklogo.com/images/G/google-ai-logo-996E85F6FD-seeklogo.com.png",
    layout="wide",
)

hide_style = """
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
  """

st.markdown(hide_style, unsafe_allow_html = True)

def main():
    st.title("Math Formula Extractor")
    st.markdown("Analyses the math formula present in an image and extracts it from the image.\nThis website uses Gemini-pro-vision model to analyze and extract the formulae from an image.")
    st.markdown("To use this website, please upload the image below (Image should be of type jpg/jpeg/png):")

    # Image upload section
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    st.write("--------------------------------------------------------------------------------------")
    processing_done = False  # Flag to track whether processing is done

    if uploaded_file:
        st.write("Here is the image uploaded:")
        st.image(uploaded_file)
        st.write("--------------------------------------------------------------------------------------")
        with st.spinner("We are processing the image, please wait..."):
          api_key = os.getenv('GEMINI_API_KEY')
          genai.configure(api_key=api_key)
        
          # Convert the uploaded file to a PIL.Image.Image object
          pil_image = Image.open(uploaded_file)
        
          # Process the image and extract the mathematical formulae present in it
          model = genai.GenerativeModel('gemini-pro-vision')
          response = model.generate_content(["Extract all the mathematical formulae present in the given image and convert it into LaTeX text and give each formula in a separate line. If there is no mathematical formula in the image just return \'No formula present in the image!\'", pil_image])
        
        # Convert the extracted formulas to LaTeX format
          latex_code = response.text
        
        # Set the flag to indicate processing is done
        processing_done = True

    # Display the download button only if processing is done
        if  "No formula present in the image!" not in latex_code and processing_done:
            st.write("The formulae found in text are:")
            st.markdown(latex_code)
            st.write("--------------------------------------------------------------------------------------")
            st.write("The LaTeX format of the formulae is:")
            st.code(latex_code)
            st.download_button(
                label="Download LaTeX File",
                data=latex_code,
                file_name="output_formula.tex",
            )
        else:
            st.code("No formula found in the image!!")

if __name__ == "__main__":
    main()
