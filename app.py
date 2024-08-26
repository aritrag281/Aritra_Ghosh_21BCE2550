# app.py

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, emit
from models import db, User
from game_logic import GameState
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ebddb950236ea849cde0ffe77886865d886b41d2544fce0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

socketio = SocketIO(app)

game_state = GameState()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('game'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/game')
@login_required
def game():
    return render_template('game.html', username=current_user.username)

@socketio.on('connect')
def handle_connect():
    emit('init', {'board': game_state.board, 'history': game_state.move_history})

@socketio.on('move')
def handle_move(data):
    character_name = data['character']
    direction = data['direction']
    if game_state.is_valid_move(character_name, direction):
        game_state.update_state(character_name, direction)
        emit('update', {'board': game_state.board, 'history': game_state.move_history}, broadcast=True)
    else:
        emit('invalid_move', {'error': 'Invalid move'})

@socketio.on('chat_message')
def handle_chat_message(data):
    emit('chat_message', {'user': data['user'], 'message': data['message']}, broadcast=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
