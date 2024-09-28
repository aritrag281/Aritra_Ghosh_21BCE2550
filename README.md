
**Pawns & Heroes - Chess-like Game - Hitwicket Software Development Task**
****

**IMPLEMENTED ALL THE BONUS CHALLENGES**

🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
Working Video of the Hitwicket Software Engineering Task - [https://drive.google.com/file/d/1r77Uk91sRDrZqnS3fNnO7zi_3-2sYKKX/view?usp=sharing
](https://drive.google.com/file/d/1Kk3dgh8Jc5pXeVxH86sJVEhiCyXZl6Rn/view?usp=sharing)

**IMPLEMENTED ALL THE BONUS CHALLENGES**

## Description
This project is a web-based chess-like game using Flask, Flask-SocketIO, and SQLAlchemy. It allows users to log in, play a game, and track moves with real-time updates.

Designed a web-based real-time strategy game using Flask, Flask-SocketIO, and SQLAlchemy, enabling users to log in, play, and
track moves with real-time updates through a server-client architecture.Developed a web client with interactive features, including clickable character pieces, valid move indicators, and move history logging, utilizing websockets for seamless communication with the server. **Implemented an AI opponent capable of playing the game using basic strategy, integrating machine learning algorithms to enhance gameplay and provide a challenging experience for users**

**IMPLEMENTED ALL THE BONUS CHALLENGES**

1 Implement additional character types with unique move patterns.
Add Hero3:
Movement: Moves 2 steps straight and one to the side in a single turn.
Attack: Kills only the character at its final landing position (if occupied by an opponent).
Move commands:
FL: 2 steps Forward, 1 step Left
FR: 2 steps Forward, 1 step Right
BL: 2 steps Backward, 1 step Left
BR: 2 steps Backward, 1 step Right
RF: 2 steps Right, 1 step Forward
RB: 2 steps Right, 1 step Backward
LF: 2 steps Left, 1 step Forward
LB: 2 steps Left, 1 step Backward
Example moves: H3:FR (2 front, 1 right), H3:RF (2 right, 1 front)

2 Implement a dynamic team composition feature:
Allow players to choose their team composition at the start of each game.
Ensure the game logic can handle any combination of character types.

3 Add a spectator mode for other clients to watch ongoing games.

4 Implement a chat feature for players to communicate during the game.

5 Create an AI opponent that can play the game using basic strategy.

6 Implement a replay system that allows players to review past games move by move.

7 Add a ranking system that tracks player performance across multiple games.


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
