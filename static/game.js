// game.js

const socket = io();
let selectedCharacter = null;

socket.on('init', (data) => {
    renderBoard(data.board);
    renderMoveHistory(data.history);
});

socket.on('update', (data) => {
    renderBoard(data.board);
    renderMoveHistory(data.history);
});

socket.on('invalid_move', (data) => {
    alert(data.error);
});

socket.on('chat_message', (data) => {
    const chatHistory = document.getElementById('chat-history');
    chatHistory.innerHTML += `<p><strong>${data.user}:</strong> ${data.message}</p>`;
    chatHistory.scrollTop = chatHistory.scrollHeight;
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
}

function renderMoveHistory(history) {
    const moveHistory = document.getElementById('move-history');
    moveHistory.innerHTML = '';
    history.forEach((entry) => {
        const p = document.createElement('p');
        p.textContent = entry;
        moveHistory.appendChild(p);
    });
    moveHistory.scrollTop = moveHistory.scrollHeight;
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
        socket.emit('move', { character: selectedCharacter, direction });
        selectedCharacter = null;
        document.querySelectorAll('.cell').forEach(c => c.classList.remove('selected'));
    } else {
        alert('No character selected!');
    }
}

function sendMessage() {
    const messageInput = document.getElementById('chat-message');
    const message = messageInput.value;
    if (message.trim()) {
        socket.emit('chat_message', { user: window.username, message });
        messageInput.value = '';
    }
}
