let body = document.body;

let columns = 9;
let rows = 6;
let cellWidth = 70;
let cellHeight = 60;
let currentImg;
let imgsList = [];

let img = document.createElement('img');
img.classList.add('example');

let borderImg = document.createElement('div');
borderImg.classList.add('border-image');

let buttonShow = document.createElement('button');
buttonShow.classList.add('button-show');
buttonShow.addEventListener('click', showImg);
buttonShow.textContent = 'Показать';

let fieldPartImg = document.createElement('div');
fieldPartImg.classList.add('field-part');


function showImg(){
    img.classList.remove('example');
    img.classList.add('example-show');
}
function hideImg(){
    img.classList.remove('example-show');
    img.classList.add('example');
}
function dragImg(event){
    currentImg = event.target;
}
function letDrop(event){
    event.preventDefault();
}
function dropImg(event){
    if (event.target.id == currentImg.id){
        event.target.classList.add('empty-tile-visible');
        currentImg.remove();
    }
    else{
        currentImg = '';
    }
    if (Array.from(document.getElementsByClassName('empty-tile-visible')).length == 54){
        img.classList.add('example-show');
    }
}

for (let i=0; i<rows; i++){
    for (let j=0; j<columns; j++){
        let emptyTile = document.createElement('div');
        emptyTile.classList.add('empty-tile');   
        emptyTile.style.backgroundPositionX = j*(-cellWidth) + 'px';
        emptyTile.style.backgroundPositionY = i*(-cellHeight) + 'px';
        emptyTile.addEventListener('dragover', letDrop);
        emptyTile.addEventListener('drop', dropImg);
        borderImg.append(emptyTile);
        emptyTile.id = j + 'x' + i;

        let partImg = document.createElement('div');
        partImg.classList.add('part-img');   
        partImg.style.backgroundPositionX = j*(-cellWidth) + 'px';
        partImg.style.backgroundPositionY = i*(-cellHeight) + 'px';
        partImg.id = j + 'x' + i;
        partImg.draggable = true;
        partImg.addEventListener('mousedown', hideImg);
        partImg.addEventListener('drag', dragImg);
        imgsList.push(partImg);
    }
}
for (let i = 0; i < 54; i++){
    let rand = Math.floor(Math.random() * imgsList.length);
    fieldPartImg.append(imgsList[rand]);
    imgsList.splice(rand, 1);
}
console.log(fieldPartImg.childNodes);
borderImg.append(img);
body.append(borderImg);
body.append(buttonShow);
body.append(fieldPartImg);
