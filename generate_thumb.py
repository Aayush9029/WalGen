# generate thumbnails for all images in the docs/images folder

import os

from PIL import Image

def main():
    # get all files in the docs/images folder
    files = os.listdir('./docs/images')

    # loop through each file
    for index, file in enumerate(files):
        # check if the file is a png
        if file.endswith("png"):
            # open the image
            img = Image.open('./docs/images/' + file)
            # resize the image to be 240x135 16:9
            img.thumbnail((240, 135))
            img.save('./docs/thumb/' + file)
        print(f" Saved thumbnail, {index} of {len(files)}, named:" + file, end='\r')


if __name__ == '__main__':
    main()
