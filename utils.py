import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# --- API KEY HANDLING ---
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- HELPER FUNCTION ---
def get_gemini_response(input_prompt, image_list):
    """
    Function to get response from Gemini, now handling multiple images.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Error: This application will be fixed shortly. Please contact the developer for assistance."
        
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    content = [input_prompt] + image_list
        
    try:
        response = model.generate_content(content)
        return response.text
    except Exception as e:
        if "API key not valid" in str(e):
            return "Error: This application will be fixed shortly. Please contact the developer for assistance."
        return f"An error occurred: {e}"