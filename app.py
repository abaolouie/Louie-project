import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

with st.container():
    st.subheader("Hi, I am John Louie :wave:")
    st.title("A student of SURIGAO STATE UNIVERSITY.")
    st.write(
        "Welcome to my home page."
    )
    st.write("My github account[Learn More >](https://github.com/abaolouie/Louie-project)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Information About me.")
        st.write("##")
        st.write(
            """
            - I am John Louie B. Abao
            - I am 18 Yeaars old
            - From linnonggaan San francisco Surigao,Del,norte
            - For now I am studying python and other languages
            - I am still single and I am waiting for someome who can accept and loving me!

            """
        )
        st.write("[Facebook Account >](https://www.facebook.com/johnlouie.abao.1)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
        
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/johnlouieabao643@gmail.comYOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
