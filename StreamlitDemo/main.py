import streamlit as st
from PIL import Image

# you need to install two dependencies first, to do so enter into terminal:
# pip3 install -r requirements.txt

# to run the app enter into terminal: streamlit run main.py
# the window should appear in your browser, if not go to http://localhost:8501/

# example for including an image
image = Image.open('wispermed.png')
st.image(image)

# example for different text inputs
st.title("Streamlit Demo")
st.header("for WisPerMed hackathon")
st.subheader("A short example for a python streamlit app")

st.write("For more infos on how to put text in your app click [here](https://docs.streamlit.io/library/api-reference/text).")
st.write("For more infos on media elements click [here](https://docs.streamlit.io/library/api-reference/media).")

writtenText = st.text_input("Write something!")

# example radio button
option = st.radio(
    'What should happen?',
    ('Just display', 'Count characters', 'Upper case'))

if writtenText == "":
    st.write("You need to enter something above...")
else:
    if option == 'Just display':
        st.write(writtenText)
    elif option == 'Count characters':
        st.write("The length of the input is " + str(len(writtenText)) + " (including whitespaces).")
    elif option == 'Upper case':
        st.write(writtenText.upper())
