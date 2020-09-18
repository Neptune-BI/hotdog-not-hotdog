import os
import pandas as pd
import base64


classes = os.listdir("./images")


with open("dataset.csv", "w") as f:
    f.write("target,image_path\n")
    for class_value in classes:
        path = os.path.join("images", class_value)
        for images in os.listdir(path):
            image_path = os.path.join(path, images)
            f.write("{},{}\n".format(class_value, image_path))

def convert_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string
 
df = pd.read_csv("dataset.csv")

df["image"] = df["image_path"].apply(lambda x: convert_to_base64(x))
df.to_csv("dataset_v2.csv",index=False)

