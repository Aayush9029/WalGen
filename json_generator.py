# Generate json from images in docs/images and save to docs/images.json

import json
from os import listdir

def main():
    """
    json struct:
    {
        "name": "",
        "data": {
            "index": 0,
            "highres": "./images/ability.png",
            "thumb": "./thumb/ability.png"
        }
    """

    files = listdir('./docs/images')
    json_data = []
    # sort files by name
    files.sort()
    index = 0
    for file in files:
        if file.endswith("png"):
            json_data.append({
                "name": file.split(".")[0],
                "data": {
                    "highres": "./images/" + file,
                    "thumb": "./thumb/" + file
                }
            })
            index += 1

    with open('docs/images.json', 'w') as f:
        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    main()
