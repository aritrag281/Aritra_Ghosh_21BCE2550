
Pawns & Heroes - Chess-like Game - Hitwicket Software Development Task
****

🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
Working Video of the Hitwicket Software Enngineering Task - https://drive.google.com/file/d/1r77Uk91sRDrZqnS3fNnO7zi_3-2sYKKX/view?usp=sharing

## Description
This project is a web-based chess-like game using Flask, Flask-SocketIO, and SQLAlchemy. It allows users to log in, play a game, and track moves with real-time updates.

Designed a web-based real-time strategy game using Flask, Flask-SocketIO, and SQLAlchemy, enabling users to log in, play, and
track moves with real-time updates through a server-client architecture.Developed a web client with interactive features, including clickable character pieces, valid move indicators, and move history logging, utilizing websockets for seamless communication with the server. **Implemented an AI opponent capable of playing the game using basic strategy, integrating machine learning algorithms to enhance gameplay and provide a challenging experience for users**

Bonus Features Implemented

2. Implement a dynamic team composition feature:
○ Allow players to choose their team composition at the start of each game.
○ Ensure the game logic can handle any combination of character types.
3. Add a spectator mode for other clients to watch ongoing games.
4. Implement a chat feature for players to communicate during the game.
5. Create an AI opponent that can play the game using basic strategy

## Setup

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the project directory:**
    ```bash
    cd <project_directory>
    ```

3. **Create a virtual environment:**
    * **On Windows:**
      ```bash
      python -m venv venv
      ```
    * **On macOS/Linux:**
      ```bash
      python3 -m venv venv
      ```

4. **Activate the virtual environment:**
    * **On Windows:**
      ```bash
      .\venv\Scripts\activate
      ```
    * **On macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the application:**
    ```bash
    python app.py
    ```

## Usage

* **Login**: Go to `/login` to log in.
* **Sign Up**: Go to `/signup` to create a new account.
* **Play Game**: After logging in, go to `/game` to start playing.

## Features

* **Real-time gameplay** with Flask-SocketIO.
* **Move history** tracking.
* **Game end notifications** with winner announcement.

## License
This project is licensed under the MIT License.
