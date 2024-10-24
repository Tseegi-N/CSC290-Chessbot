import chess
import random
from datetime import datetime

white_moves = [
        "g2g4",
        "f2f3"  # White moves pawn from f2 to f3
           # White moves pawn from g2 to g4
    ]

black_moves = [
        "e7e5",  # Black moves pawn from e7 to e5
        "d8h4"   # Black moves queen from d8 to h4 (checkmate)
    ]

def winner(outcome):
    if outcome.winner is chess.WHITE:
        return "White wins!"
    elif outcome.winner is chess.BLACK:
        return "Black wins"
    else:
        return "It's a draw."
# Move board pieces
def bot_move(board):
    legal_moves = list(board.legal_moves)
    capture_moves = []

    #check for capture 
    for moves in legal_moves:
        if board.is_capture(moves):
            capture_moves.append(moves)
    
    if capture_moves != []:
        next_move = capture_moves[random.randint(0, len(capture_moves)-1)]
    else:
        next_move = legal_moves[random.randint(0, len(legal_moves)-1)]
    
    return next_move
def bot_move_test(moves):
    next_move = moves[0]
    next_move = chess.Move.from_uci(next_move)
    moves.pop(0)
    return next_move

def play_chess_test():
    print(datetime.now())
    bot_color = input("Computer Player? (w=white/b=black): ").lower()

    if bot_color not in ['w', 'b']:
        print("Please choose white or black. ")
        bot_color = input("Computer Player? (w=white/b=black): ").lower()

    # User color
    if bot_color == 'w':
        user_color = 'b'
    else:
        user_color = 'w'
    fen_start_pos = input("Starting FEN position? (hit ENTER for standard starting postion): ")

    if fen_start_pos == "":
        board = chess.Board()
    else:
        board = chess.Board(fen_start_pos)

    # Game loop 
    while board.is_game_over() == False:
        # Bots turn
        if (bot_color == 'w' and board.turn == chess.WHITE) or (bot_color == 'b' and board.turn == chess.BLACK):
            moves = []
            if  bot_color =='w':
                moves = white_moves
            else:
                moves = black_moves

            move = bot_move_test(moves)
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
    outcome = board.outcome()
    if board.is_checkmate:
        print("Checkmate!")
    elif board.is_stalemate:
        print("Stalemate!")
    elif board.is_insufficient_material():
        print("Insuficient Material!")
    print(winner(outcome))

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
    outcome = board.outcome()
    if board.is_checkmate:
        print("Checkmate!")
    elif board.is_stalemate:
        print("Stalemate!")
    elif board.is_insufficient_material():
        print("Insuficient Material!")
    print(winner(outcome))

def main(): 
    play_chess()
    # play_chess_test()
    
main()