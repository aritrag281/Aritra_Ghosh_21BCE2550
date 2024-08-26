const socket = io();
let selectedCharacter = null;

socket.on('init', (data) => {
    renderBoard(data.board);
    renderMoveHistory(data.history);
    if (data.winner) {
        alert(`Player ${data.winner} wins!`);
    }
});

socket.on('update', (data) => {
    renderBoard(data.board);
    renderMoveHistory(data.history);
    if (data.winner) {
        alert(`Player ${data.winner} wins!`);
    }
});

socket.on('invalid_move', (data) => {
    alert(data.error);
});

function renderBoard(board) {
    const gameBoard = document.getElementById('game-board');
    gameBoard.innerHTML = '';
    board.forEach((row, i) => {
        row.forEach((cell, j) => {
            const div = document.createElement('div');
            div.classList.add('cell');
            if (cell.includes('Pawn')) {
                div.classList.add('pawn');
            } else if (cell.includes('Hero1') || cell.includes('Hero2')) {
                div.classList.add('hero1');
            }
            div.textContent = cell;
            div.addEventListener('click', () => handleCellClick(cell));
            gameBoard.appendChild(div);
        });
    });
    console.log('Board rendered:', board);
}

function renderMoveHistory(history) {
    const historyDiv = document.getElementById('move-history');
    historyDiv.innerHTML = '';
    history.forEach((move) => {
        const p = document.createElement('p');
        p.textContent = move;
        historyDiv.appendChild(p);
    });
}

function handleCellClick(cell) {
    const cells = document.querySelectorAll('.cell');
    cells.forEach(c => c.classList.remove('selected'));
    
    if (selectedCharacter === cell) {
        selectedCharacter = null;
    } else {
        selectedCharacter = cell;
        const selectedCells = Array.from(cells).filter(c => c.textContent === selectedCharacter);
        selectedCells.forEach(c => c.classList.add('selected'));
    }
}

function makeMove(direction) {
    if (selectedCharacter) {
        console.log(`Sending move: ${selectedCharacter}, ${direction}`);
        socket.emit('move', { character: selectedCharacter, direction });
        selectedCharacter = null;
        document.querySelectorAll('.cell').forEach(c => c.classList.remove('selected'));
    } else {
        alert('No character selected!');
    }
}
