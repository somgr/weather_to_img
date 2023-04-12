from PIL import Image
import os

def edit_photo(p):
    image_path = p

    img = Image.open(image_path)

    new_image = img.resize((472, 590))

    new_image.save(f'{image_path}')


for filename in os.listdir('photo'):
    edit_photo(f'photo/{filename}')