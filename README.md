# Chess-like Game

## Description
This project is a web-based chess-like game using Flask, Flask-SocketIO, and SQLAlchemy. It allows users to log in, play a game, and track moves with real-time updates.

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
