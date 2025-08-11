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
- **LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile) (*Please update with your LinkedIn profile*)
- **GitHub:** [github.com/yourusername](https://github.com/yourusername) (*Please update with your GitHub profile*)
""")

st.subheader("Send me a message")
contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
