import pygame
import sys
import math
import random

pygame.init()
pygame.mixer.init()

class TicTacToe:
    
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
        self.current_winner = None

    def draw_board(self, screen):
        for i in range(1, 3):
            pygame.draw.line(screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 5)
            pygame.draw.line(screen, (0, 0, 0), (0, i * 200), (600, i * 200), 5)

        for row_num, row in enumerate([self.board[i * 3:(i + 1) * 3] for i in range(3)]):
            for col_num, spot in enumerate(row):
                if spot == 'X':
                    pygame.draw.line(screen, (0, 0, 0), (col_num * 200 + 50, row_num * 200 + 50), (col_num * 200 + 150, row_num * 200 + 150), 5)
                    pygame.draw.line(screen, (0, 0, 0), (col_num * 200 + 150, row_num * 200 + 50), (col_num * 200 + 50, row_num * 200 + 150), 5)
                elif spot == 'O':
                    pygame.draw.circle(screen, (0, 0, 0), (col_num * 200 + 100, row_num * 200 + 100), 70, 5)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return letter
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return letter
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return letter
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return letter
        return None

    def evaluate(self):
        winner = self.winner_for_evaluation()
        if winner == 'O':
            return 1  
        elif winner == 'X':
            return -1  
        else:
            return 0  

    def winner_for_evaluation(self):
        for row in range(0, 9, 3):
            if self.board[row] == self.board[row + 1] == self.board[row + 2] != ' ':
                return self.board[row]
        for col in range(3):
            if self.board[col] == self.board[col + 3] == self.board[col + 6] != ' ':
                return self.board[col]
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        return None

def alpha_beta(position, depth, alpha, beta, maximizing_player, game):
    if depth == 0 or game.num_empty_squares() == 0 or game.winner_for_evaluation():
        return game.evaluate(), position

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'O')
            if game.winner(move, 'O'):
                game.board[move] = ' '
                return 1, move  
            eval, _ = alpha_beta(move, depth-1, alpha, beta, False, game)
            game.board[move] = ' '
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'X')
            if game.winner(move, 'X'):
                game.board[move] = ' '
                return -1, move  
            eval, _ = alpha_beta(move, depth-1, alpha, beta, True, game)
            game.board[move] = ' '
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval, best_move

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_start_screen(screen, width, height):
    screen.fill((255, 255, 255))
    draw_text(screen, "Welcome to Tic Tac Toe!", 48, (0, 0, 0), width // 2, height // 2 - 50)
    draw_text(screen, "Press any key to start", 36, (0, 0, 0), width // 2, height // 2 + 50)
    pygame.display.flip()
    wait_for_key()

def draw_end_screen(screen, message, width, height):
    screen.fill((255, 255, 255))
    draw_text(screen, message, 48, (255, 0, 0), width // 2, height // 2 - 50)
    draw_text(screen, "Press R to restart or Q to quit", 36, (0, 0, 0), width // 2, height // 2 + 50)
    pygame.display.flip()
    wait_for_restart_or_quit()

def draw_score_screen(screen, player_wins, ai_wins, draws, width, height):
    screen.fill((255, 255, 255))
    draw_text(screen, "Score", 48, (0, 0, 0), width // 2, height // 2 - 100)
    draw_text(screen, f"You: {player_wins}", 36, (0, 0, 0), width // 2, height // 2 - 50)
    draw_text(screen, f"AI: {ai_wins}", 36, (0, 0, 0), width // 2, height // 2)
    draw_text(screen, f"Draws: {draws}", 36, (0, 0, 0), width // 2, height // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(2000)  

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def wait_for_restart_or_quit():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    return False

def play():
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tic Tac Toe")

    player_wins = 0
    ai_wins = 0
    draws = 0

    while True:
        draw_start_screen(screen, width, height)

        game = TicTacToe()

        beep_sound = pygame.mixer.Sound("beep.wav")

        player_turn = random.choice(['X', 'O'])

        if player_turn == 'O':
            _, computer_move = alpha_beta(-1, game.num_empty_squares(), -math.inf, math.inf, True, game)
            game.make_move(computer_move, 'O')
            player_turn = 'X'  

        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and player_turn == 'X':
                    mouseX, mouseY = event.pos
                    square = (mouseY // 200) * 3 + (mouseX // 200)
                    if game.make_move(square, 'X'):
                        player_move_sound = pygame.mixer.Sound("drawX.wav")
                        player_move_sound.play()

                        if game.winner_for_evaluation():
                            game_over = True
                            break

                        player_turn = 'O'

            if player_turn == 'O' and game.num_empty_squares() > 0:
                _, computer_move = alpha_beta(-1, game.num_empty_squares(), -math.inf, math.inf, True, game)
                game.make_move(computer_move, 'O')
                computer_move_sound = pygame.mixer.Sound("drawO.wav")
                computer_move_sound.play()

                if game.winner_for_evaluation():
                    game_over = True
                player_turn = 'X'

            screen.fill((255, 255, 255))
            game.draw_board(screen)
            pygame.display.flip()

            if game_over:
                winner = "AI" if game.current_winner == 'O' else "You"
                if winner == "AI":
                    ai_wins += 1
                else:
                    player_wins += 1
                pygame.time.wait(300)
                draw_end_screen(screen, f"{winner} wins!", width, height)
                beep_sound.play() 
                break
            elif not game.empty_squares():
                draws += 1
                game_over = True
                pygame.time.wait(300)
                draw_end_screen(screen, "It's a draw!", width, height)
                beep_sound.play()  
                break

        draw_score_screen(screen, player_wins, ai_wins, draws, width, height)

        if not wait_for_restart_or_quit():
            break

if __name__ == "__main__":
    play()