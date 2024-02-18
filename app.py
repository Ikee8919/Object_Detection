import streamlit as st
import requests
from PIL import Image
from dotenv import load_dotenv
import io
import os


# Set up the API URL and headers with your Hugging Face API token
#API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
# Load environment variables from .env file
load_dotenv()

# Set up the API URL and use the environment variable for the API token
#API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
api_token = os.getenv("HUGGING_FACE_API_TOKEN")
print(api_token)
headers = {"Authorization": f"Bearer {api_token}"}

# (The rest of your code remains the same)
headers = {"Authorization": "Bearer YOUR_HUGGING_FACE_API_TOKEN_HERE"}

def query(image_bytes):
    response = requests.post(api_token, headers=headers, files={"file": image_bytes})
    return response.json()

# Streamlit interface
st.title("Object Detection with DETR")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")

    # Convert the image to bytes and send it to the model
    with io.BytesIO() as image_bytes:
        image.save(image_bytes, format=image.format)
        image_bytes.seek(0)  # Go to the beginning of the IO object
        st.write("Detecting objects...")
        output = query(image_bytes)
        
        # Display the results
        if output:
            st.write("Detection Results:")
            st.json(output)
        else:
            st.write("No objects detected or there was an error in detection.")

