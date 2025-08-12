import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="✉️")

st.title("✉️ Let's Connect!")

st.markdown("""I'm excited to learn about your project and how I can help you achieve your goals. 
Whether you have a question, a project proposal, or just want to say hello, please don't hesitate to reach out.
""")

st.subheader("Contact Information")
st.markdown("""
- **Name:** Tejraj Jadhav
- **Email:** tejrajjadhav.work@gmail.com
- **LinkedIn:** [linkedin.com/in/tejraj-jadhav009](https://linkedin.com/in/tejraj-jadhav009)
- **GitHub:** [github.com/TEJRAJ009](https://github.com/TEJRAJ009)
""")

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
