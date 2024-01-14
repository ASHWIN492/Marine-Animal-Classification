import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(229, 300))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Make sure to adjust the number of classes (23 in this case)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        class_labels = {
           0: 'Clams', 1: 'Corals', 2: 'Crabs', 3:'Dolphin', 4: 'Eel', 5:'Fish', 6:'Jelly Fish', 7:'Jelly Fish', 8: 'Lobster', 9:'Nudibranchs', 10:'Octopus', 11: 'Otter', 12:'Penguin', 13:'Puffers', 14:'Sea Rays', 15: 'Sea Urchins', 16:'Seahorse', 17:'Seal', 18:'Sharks', 19:'Shrimp', 20:'Squid', 21: 'Starfish',22:'Turtle_Tortoise', 23: 'Whale'
        }

        predicted_class = class_labels.get(result[0], 'Unknown Class')
        
        return [{"image": predicted_class}]
