class Character:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, direction):
        pass

class Pawn(Character):
    def move(self, direction):
        x, y = self.position
        if direction == 'up':
            return (x - 1, y)
        elif direction == 'down':
            return (x + 1, y)
        elif direction == 'left':
            return (x, y - 1)
        elif direction == 'right':
            return (x, y + 1)
        return self.position

class Hero1(Character):
    def move(self, direction):
        x, y = self.position
        if direction == 'left':
            return (x, y - 2)
        elif direction == 'right':
            return (x, y + 2)
        elif direction == 'up':
            return (x - 2, y)
        elif direction == 'down':
            return (x + 2, y)
        return self.position

class Hero2(Character):
    def move(self, direction):
        x, y = self.position
        if direction == 'left':
            return (x - 1, y - 1)
        elif direction == 'right':
            return (x - 1, y + 1)
        elif direction == 'up':
            return (x - 1, y)
        elif direction == 'down':
            return (x + 1, y)
        return self.position

class GameState:
    def __init__(self):
        self.board = [['' for _ in range(5)] for _ in range(5)]
        self.turn = 'A'
        self.players = {'A': [], 'B': []}
        self.history = []
        self.initialize_board()

    def initialize_board(self):
        self.players['A'].append(Pawn('A_Pawn', (4, 0)))
        self.players['A'].append(Hero1('A_Hero1', (4, 1)))
        self.players['A'].append(Hero2('A_Hero2', (4, 2)))

        self.players['B'].append(Pawn('B_Pawn', (0, 4)))
        self.players['B'].append(Hero1('B_Hero1', (0, 3)))
        self.players['B'].append(Hero2('B_Hero2', (0, 2)))

        for player in self.players:
            for character in self.players[player]:
                x, y = character.position
                self.board[x][y] = character.name

    def is_valid_move(self, character_name, direction):
        character = self.get_character(character_name)
        if not character:
            return False

        new_position = character.move(direction)
        x, y = new_position

        if x < 0 or x >= 5 or y < 0 or y >= 5:
            return False  # Out of bounds
        if self.board[x][y] != '':
            return False  # Cell already occupied
        return True

    def update_state(self, character_name, direction):
        character = self.get_character(character_name)
        if not character:
            return

        old_position = character.position
        new_position = character.move(direction)

        if new_position[0] < 0 or new_position[0] >= 5 or new_position[1] < 0 or new_position[1] >= 5:
            return

        self.board[old_position[0]][old_position[1]] = ''
        self.board[new_position[0]][new_position[1]] = character.name
        character.position = new_position

        # Combat check
        if self.check_combat(new_position):
            self.remove_character(new_position)

        # Check for win condition
        winner = self.check_win()
        if winner:
            return winner

        # Switch turn
        self.turn = 'B' if self.turn == 'A' else 'A'
        self.history.append(f"{self.turn} moved {character_name} {direction}")
        print(f"Updated board: {self.board}")  # Debugging statement

    def get_character(self, character_name):
        for player in self.players:
            for character in self.players[player]:
                if character.name == character_name:
                    return character
        return None

    def check_combat(self, position):
        x, y = position
        for player in self.players:
            for character in self.players[player]:
                if character.position == (x, y):
                    # Combat: remove opponent's character
                    if player != self.turn:
                        return True
        return False

    def remove_character(self, position):
        x, y = position
        for player in self.players:
            for character in self.players[player]:
                if character.position == (x, y):
                    self.players[player].remove(character)
                    self.board[x][y] = ''
                    break

    def check_win(self):
        if not self.players['A']:
            return 'B'
        if not self.players['B']:
            return 'A'
        return None
