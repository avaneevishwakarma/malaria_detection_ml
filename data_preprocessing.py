import cv2
import numpy as np
import os

data_dir = "cell_images"

images = []
labels = []

for category in ["Parasitized","Uninfected"]:
    path = os.path.join(data_dir, category)
    label = 1 if category == "Parasitized" else 0

    for img in os.listdir(path):
        img_path = os.path.join(path,img)
        image = cv2.imread(img_path)
        image = cv2.resize(image,(64,64))
        images.append(image)
        labels.append(label)

X = np.array(images)/255.0
y = np.array(labels)

print("Data preprocessing completed")
