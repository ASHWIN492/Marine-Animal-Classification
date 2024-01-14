import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


model_path = "C:/Users/ashwi/OneDrive/Desktop/devrev07_1/under-water-animal-classification/artifacts/training/model.h5"
model = load_model(model_path)


class_labels = {
    0: 'Clams', 1: 'Corals', 2: 'Crabs', 3: 'Dolphin', 4: 'Eel', 5: 'Fish', 6: 'Jelly Fish',
    7: 'Jelly Fish', 8: 'Lobster', 9: 'Nudibranchs', 10: 'Octopus', 11: 'Otter', 12: 'Penguin',
    13: 'Puffers', 14: 'Sea Rays', 15: 'Sea Urchins', 16: 'Seahorse', 17: 'Seal', 18: 'Sharks',
    19: 'Shrimp', 20: 'Squid', 21: 'Starfish', 22: 'Turtle_Tortoise', 23: 'Whale'
}

def classify_image(img):
    img = img.resize((300, 229))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0 

   
    prediction = model.predict(img)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels.get(predicted_class_index, 'Unknown Class')
    confidence = prediction[0][predicted_class_index] * 100  

    return predicted_class, confidence

def main():
    st.title("Image Classification App")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        
        image_display = Image.open(uploaded_file)
        st.image(image_display, caption="Uploaded Image", use_column_width=True)

        
        predicted_class, confidence = classify_image(image_display)

        
        st.success(f"Prediction: {predicted_class}")
        st.info(f"Confidence: {confidence:.2f}%")

if __name__ == "__main__":
    main()
