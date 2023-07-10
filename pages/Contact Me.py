import streamlit as st
from send_email import send_email

st.title("Contact Me")

# st.write("Feel free to reach out to me at tsreeni21@gmail.com")
with st.form(key="contact_form"):
    user_email = st.text_input("Your email address: ", key="email")
    user_message = st.text_area("Your message: ", key='message')
    button = st.form_submit_button("Submit")
    if button:
        # message = user_email+"\n"+user_message
        message = f"""Subject: New email from your portfolio app!

From: {user_email}
{user_message}
"""
        print(message)
        send_email(message)