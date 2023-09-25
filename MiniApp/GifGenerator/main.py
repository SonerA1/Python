import imageio
from PIL import Image

image_list = list()
frames = list()

while True:
    images = input("") #images filepath
    if images == "q":
        break
    else:
        image_list.append(images)

for image_path in image_list:
    img = Image.open(image_path)
    resized_img = img.resize((400, 400))
    frames.append(resized_img)

imageio.mimsave("animasyon.gif", frames, format="GIF", duration=3)