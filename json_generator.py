import json
from os import listdir


def main():
    """
    json struct:
    {   
        'index' : ''
        'name' : '',
        'path' : ''
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
                'index':index,
                'name' : file.split('.')[0].title(),
                'path' : './images/' + file
            })
            index += 1

    with open('docs/images.json', 'w') as f:
        json.dump(json_data, f, indent=4)


if __name__ == '__main__':
    main()
