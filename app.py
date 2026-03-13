import cv2
import numpy as np

def predict_cell(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img,(64,64))
    img = img/255.0
    img = np.reshape(img,(1,64,64,3))

    print("Prediction complete")

predict_cell("test_image.png")
