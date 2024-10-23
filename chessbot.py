import chess
import random
from datetime import datetime

# Move board pieces
def bot_move(board):
    legal_moves = list(board.legal_moves)

    #check for capture 
    

def play_chess():
    # Print messages 
    print(datetime.now)

    # Choose color
    bot_color = input("Computer Player? (w=white/b=black): ").strip.lower()

    if bot_color not in ['w', 'b']:
        print("Please choose white or black. ")
        bot_color = input("Computer Player? (w=white/b=black): ").strip.lower()

    # User color
    if bot_color == 'w':
        user_color = 'b'
    else:
        user_color = 'w'

    # Obtain fen position
    fen_start_pos = input("Starting FEN position? (hit ENTER for standard starting postion): ")

    if fen_start_pos == "":
        board = chess.Board()
    else:
        board = chess.Board(fen_start_pos)

    # Game loop 
    while board.is_game_over() == False:
        # Bots turn
        if (bot_color == 'w' and board.turn == chess.WHITE) or (bot_color == 'b' and board.turn == chess.BLACK):
            move = bot_move(board)
            board.push(move)

        # Users turn
        else:
            user_move = input("Your move as a ", user_color, " : ").strip()
            if user_move in board.legal_moves:
                board.push(user_move)
                print("New FEN position: ", board.fen())
            else:
                print("Invalid move. Please try again.")

        # Game over

