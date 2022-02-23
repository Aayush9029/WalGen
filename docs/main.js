const json_file = './images.json';
const high_res_path = './images/';

let images_json;

createImageDiv = (name, url) => {


    const div = document.createElement('div');
    div.id = 'thumb_container';

    const image = document.createElement('img');
    image.id = 'thumb_image';
    image.src = url;
    image.alt = name;

    const name_div = document.createElement('h5');
    name_div.id = 'thumb_name';
    name_div.innerText = name;

    div.appendChild(image);
    div.appendChild(name_div);


    div.onclick = () => {
        const hi_res_url = high_res_path + name + '.png';
        window.open(hi_res_url, '_blank');
    };
    return div;
}

appendImage = (name, url) => {
    const parent = document.getElementById('container')
    const div = createImageDiv(name, url);
    parent.appendChild(div);
}

appendImages = (json) => {
    json.forEach(element => {
        appendImage(element.name, element.data.thumb);
    });
}

// MAIN FUNCTION

fetch(json_file)
    .then(response => response.json())
    .then(jsonResponse => appendImages(jsonResponse));