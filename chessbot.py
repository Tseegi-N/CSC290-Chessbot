import chess
import random
from datetime import datetime

# Move board pieces
def bot_move(board):
    legal_moves = list(board.legal_moves)
    capture_moves = []

    #check for capture 
    for moves in legal_moves:
        if board.is_capture(moves):
            capture_moves.append(moves)
    
    if capture_moves != []:
        next_move = capture_moves[random.randint(0, len(capture_moves))]
    else:
        next_move = legal_moves[random.randint(0, len(legal_moves))]
    
    return next_move

def play_chess():
    # Print messages 
    print(datetime.now())

    # Choose color
    bot_color = input("Computer Player? (w=white/b=black): ").lower()

    if bot_color not in ['w', 'b']:
        print("Please choose white or black. ")
        bot_color = input("Computer Player? (w=white/b=black): ").lower()

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
            print("Bot move as a ", bot_color, " : ", move)
            board.push(move)
            print("New FEN position: ", board.fen())

        # Users turn
        else:
            user_move = input("Your move as a "+ user_color+ " : ")
            user_move = chess.Move.from_uci(user_move)
            if user_move in board.legal_moves:
                board.push(user_move)
                print("New FEN position: ", board.fen())
            else:
                print("Invalid move. Please try again.")

    # Game over
    if board.is_checkmate == True:
        print("Checkmate")
    if board.is_stalemate == True:
        print("Stalemate")

def main(): 
    play_chess()

main()