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
        self.move_history = []
        self.winner = None
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
            if self.board[x][y][0] == character_name[0]:
                return False  # Target cell occupied by friendly character

        return True

    def check_combat(self, old_position, new_position):
        if self.board[new_position[0]][new_position[1]] != '':
            enemy_name = self.board[new_position[0]][new_position[1]]
            enemy_player = enemy_name[0]
            if enemy_player != self.turn:
                self.board[new_position[0]][new_position[1]] = ''
                return True
        return False

    def check_win(self):
        player_a_alive = any(c.name.startswith('A_') for c in self.players['A'])
        player_b_alive = any(c.name.startswith('B_') for c in self.players['B'])
        
        if not player_a_alive:
            self.winner = 'B'
        elif not player_b_alive:
            self.winner = 'A'

    def update_state(self, character_name, direction):
        character = self.get_character(character_name)
        if not character:
            return False

        old_position = character.position
        new_position = character.move(direction)

        if not self.is_valid_move(character_name, direction):
            return False

        if not (0 <= new_position[0] < 5 and 0 <= new_position[1] < 5):
            return False

        if self.check_combat(old_position, new_position):
            self.board[old_position[0]][old_position[1]] = ''
        self.board[old_position[0]][old_position[1]] = ''
        self.board[new_position[0]][new_position[1]] = character_name
        character.position = new_position

        self.move_history.append(f'{self.turn} moved {character_name} to {direction}')
        self.check_win()
        self.turn = 'B' if self.turn == 'A' else 'A'
        return True

    def get_character(self, character_name):
        for player in self.players:
            for character in self.players[player]:
                if character.name == character_name:
                    return character
        return None
