let board = document.getElementsByClassName('game')[0];
let height = 12;
let width = 12;
let countBombs = 25;
let isFirstOpen = true;
let isFlag = false;
let gameOver = false;
let currentCell;

function setFlag(){
    if (this.classList[1] != 'clear' && gameOver == false){
        this.classList.toggle('flag');
    }
}

function placeBombs(cell){
    let rows = Array.from(cell.parentNode.parentNode.getElementsByClassName('row'));
    let x = Array.from(cell.parentNode.childNodes).indexOf(cell);
    let y = rows.indexOf(cell.parentNode);
    let area = [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]];
    for (let h = 0; h < countBombs; h++){
        let clearCells = document.querySelectorAll('#close');
        let rand = Math.floor(Math.random() * clearCells.length);
        let notFirstEight = true;
        for (let i = 0; i < 8; i++){
            try{
                if (clearCells[rand] == Array.from(rows[area[i][1]].childNodes)[area[i][0]]){
                    notFirstEight = false;
                    break;
                }
            }
            catch(e){
                continue;
            }
        }
        while (notFirstEight == false){
            rand = Math.floor(Math.random() * clearCells.length);
            notFirstEight = true;
            try{
                if (clearCells[rand] == Array.from(rows[area[i][1]].childNodes)[area[i][0]]){
                    notFirstEight = false;
                    break;
                }
            }
            catch(e){
                continue;
            }
        }
        clearCells[rand].classList.remove('clear');
        clearCells[rand].id = 'bomb';
    }
}

function checkBombs(cell){
    let rows = Array.from(cell.parentNode.parentElement.getElementsByClassName('row'));
    let x = Array.from(cell.parentNode.childNodes).indexOf(cell);
    let y = rows.indexOf(cell.parentElement);
    let area = [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]];
    let currentBomb = 0;
    for (let i = 0; i < 8; i++){
        try{
            if (Array.from(rows[area[i][1]].childNodes)[area[i][0]].id == 'bomb'){
                currentBomb++;
            }
        }
        catch(e){
            continue;
        }
    }
    if (currentBomb != 0){
        cell.textContent = currentBomb;
    }
    else{
        for (let i = 0; i < 8; i++){
            try{
                if (Array.from(rows[area[i][1]].childNodes)[area[i][0]].id == 'close'){
                    Array.from(rows[area[i][1]].childNodes)[area[i][0]].click();
                }
            }
            catch(e){
                    continue;
            }
        }
    }    
}

function firstOpen(cell){
    isFirstOpen = false;
    cell.classList.add('clear');
    cell.id = 'clear';
    let columnCells = Array.from(cell.parentNode.childNodes);
    let rows = Array.from(cell.parentNode.parentNode.getElementsByClassName('row'));
    let x = columnCells.indexOf(cell);
    let y = rows.indexOf(cell.parentNode);
    let area = [[x-1, y-1], [x, y-1],[x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]];
    placeBombs(cell);
    for (let i = 0; i < 8; i++){
        try{
            let row = rows[area[i][1]];
            let areaCell = row.getElementsByTagName('div')[area[i][0]];
            areaCell.click();
        }
        catch(e){
            continue;
        }
    }
}

function openCell(){
    if (gameOver == false){
        if (isFirstOpen){
            firstOpen(this);
        }
        else if (this.classList[1] == 'flag'){}
        else if (this.id == 'close'){
            this.classList.add('clear');
            this.id = 'clear';
            checkBombs(this);
        }
        else if (this.id == 'bomb' && this.classList[1] != 'flag'){
            let bombs = document.querySelectorAll('#bomb');
            for (let i = 0; i < bombs.length; i++){
                bombs[i].classList.add('bomb');
                gameOver = true;
            }
        }
        if (countBombs == height*width - document.getElementsByClassName('clear').length){
            theVictory();
        }
    }
}
for (let i = 0; i < height; i++){
    let row = document.createElement('div');
    row.classList.add('row');
    for (let j = 0; j < width; j++){
        let cell = document.createElement('div');
        cell.classList.add('cell');
        cell.setAttribute('id', 'close');
        cell.addEventListener('click', openCell);
        cell.addEventListener('contextmenu', setFlag);
        row.append(cell);
    }
    board.append(row);
}
currentCell = document.querySelector('.cell');
currentCell.classList.add('focus');
let list = Array.from(board.getElementsByTagName('div'));
let el1 = document.createElement('li');
let el2 = document.createElement('li');
let el3 = document.createElement('li');
let br = document.createElement('ul');
br.textContent = 'Правила игры для режима клавиатуры:';
el1.textContent = 'нажмите Enter или Пробел, чтобы открыть ячейку;';
el2.textContent = 'нажмите Ctrl+Enter или Ctrl+Пробел, чтобы пометить ячейку как потенциально заминированную;';
el3.textContent = 'нажмите Ctrl+R или R для перезапуска игры.';
board.append(br);
board.append(el1);
board.append(el2);
board.append(el3);

document.body.addEventListener('keydown', function(event){
    let rows = Array.from(currentCell.parentNode.parentNode.getElementsByClassName('row'));
    let x = Array.from(currentCell.parentNode.childNodes).indexOf(currentCell);
    let y = rows.indexOf(currentCell.parentNode);
    if (event.key === 'ArrowLeft'){
        currentCell.classList.remove('focus');
        x -= 1;
    }
    else if (event.key === 'ArrowRight'){
        currentCell.classList.remove('focus');
        x += 1;
    }
    else if (event.key === 'ArrowUp'){
        currentCell.classList.remove('focus');
        y -= 1;
    }
    else if (event.key === 'ArrowDown'){
        currentCell.classList.remove('focus');
        y += 1;
    }
    if (x == -1){
        x = Array.from(currentCell.parentNode.childNodes).length - 1;
    }
    if (y == -1){
        y = rows.length - 1;
    }
    if (x == Array.from(currentCell.parentNode.childNodes).length){
        x = 0;
    }
    if (y == rows.length){
        y = 0;
    }
    if (event.ctrlKey && event.key === 'Enter' || event.ctrlKey && event.code === 'Space'){
        if (currentCell.classList[1] != 'clear' && gameOver == false){
            currentCell.classList.toggle('flag');
        }
    }
    else if (event.key === 'Enter' || event.code === 'Space'){
        if (gameOver == false){
            if (isFirstOpen){
                firstOpen(currentCell);
            }
            else if (currentCell.classList[1] == 'flag'){}
            else if (currentCell.id == 'close'){
                currentCell.classList.add('clear');
                currentCell.id = 'clear';
                checkBombs(currentCell);
            }
            else if (currentCell.id == 'bomb' && currentCell.classList[1] != 'flag'){
                let bombs = document.querySelectorAll('#bomb');
                for (let i = 0; i < bombs.length; i++){
                    bombs[i].classList.add('bomb');
                    gameOver = true;
                }
            }
            if (countBombs == height*width - document.getElementsByClassName('clear').length){
                theVictory();
            }
        }
    }
    if (event.key === 'r'){
        window.location.reload();
    }
    currentCell = Array.from(rows[y].childNodes)[x];
    currentCell.classList.add('focus');      
})
document.body.addEventListener('mousedown', function(){
    currentCell.classList.remove('focus');
})
function theVictory(){
    alert('You have won!!!');
}