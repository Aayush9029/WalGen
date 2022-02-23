let json_file = './docs/images.json';

fetch(json_file)
    .then(response => response.json())
    .then(jsonResponse => console.log(jsonResponse))