from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.set_page_config(page_title="Chat With Multimodal",page_icon=":books:")
st.header("Chat With Multimodal :books:")

if not os.path.exists("uploads"):
    os.makedirs("uploads")

uploaded_image = st.text_input("insert image url")
prompt = st.text_input("insert prompt")
if uploaded_image and prompt:
    st.image(uploaded_image, caption="Your Image", use_column_width=True)
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": uploaded_image,
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    st.header("RESPONSE:")
    st.write(response.choices[0].message.content)
