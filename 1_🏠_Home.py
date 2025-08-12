import streamlit as st
from PIL import Image
from utils import get_gemini_response
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Visual-to-Viral Assistant",
    page_icon="🤖",
    layout="wide"
)

# --- MAIN APP UI ---
st.title("✍️ Visual-to-Viral E-commerce Assistant")
st.markdown("From a simple product shot to a full marketing campaign! ✨")

# --- API KEY HANDLING ---
api_key_input = st.sidebar.text_input("Enter your Google API Key", type="password")

if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input
    st.sidebar.success("API Key set successfully!")
else:
    st.sidebar.warning("To use the app, please enter your Google API Key. If you don't have one, please contact me to get access to the full application.")


# --- Layout with Columns ---
col1, col2 = st.columns([0.4, 0.6])

with col1:
    with st.expander("Step 1: Your Product Details", expanded=True):
        uploaded_files = st.file_uploader(
            "Upload product images...", 
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True
        )
        
        image_list = []
        if uploaded_files:
            for uploaded_file in uploaded_files:
                image = Image.open(uploaded_file)
                image_list.append(image)
            st.image(image_list, width=100)
        
        user_notes = st.text_area(
            "Add specific features or notes (optional)",
            placeholder="e.g., Made from 100% organic cotton, waterproof up to 50m, ships in eco-friendly packaging..."
        )

    with st.expander("Step 2: Advanced Options (Teaser)", expanded=False):
        brand_voice = st.text_input("Brand Voice (e.g., Playful, Professional, Witty)")
        target_audience = st.selectbox("Target Audience", ["Gen Z", "Millennials", "Gen X", "Baby Boomers"])
        st.info("**Unlock More Features!** Contact me to train the AI on your specific brand voice and target audience for even more effective copy.")


st.divider()

if st.button("🚀 Generate Marketing Copy", type="primary", use_container_width=True):
    if image_list:
        with st.spinner('The AI is analyzing the images and crafting copy... ✨'):
            input_prompt = f"""
            You are an expert e-commerce copywriter. Analyze the provided product images and the user's notes to generate a complete suite of marketing copy.

            **User's Notes / Key Features to Emphasize:**
            {user_notes if user_notes else "None provided. Rely primarily on the images."}

            **Brand Voice:** {brand_voice if brand_voice else "Not specified"}
            **Target Audience:** {target_audience if target_audience else "Not specified"}


            Based on the images, notes, brand voice, and target audience, generate the following in a clear, well-structured format with Markdown:

            1.  **Product Title:** An SEO-friendly title.
            2.  **Product Description:** A compelling description using bullet points for features.
            3.  **Social Media Posts (Instagram & Facebook):** Engaging captions with relevant hashtags.
            4.  **SEO Keywords:** A comma-separated list of 5-7 relevant keywords.
            """
            
            response = get_gemini_response(input_prompt, image_list)
            st.markdown(response)
    else:
        st.warning("Please upload at least one image first.")

st.sidebar.title("About the App")
st.sidebar.info("This is a demo of the Visual-to-Viral E-commerce Assistant. The full version includes advanced features like brand voice training, competitor analysis, and more.")
st.sidebar.title("Contact Me")
st.sidebar.info("Ready to take your e-commerce marketing to the next level? Contact me for a personalized demo and to discuss your specific needs.")
if st.sidebar.button("✉️ Contact Me"):
    st.switch_page("pages/2_✉️_Contact.py")
