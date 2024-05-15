import json
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or \
            board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board, symbol):
    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1
            row, col = position // 3, position % 3
            if board[row][col] == " ":
                board[row][col] = symbol
                break
            else:
                print("Position already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move(board, symbol):
    empty_positions = get_empty_positions(board)
    position = random.choice(empty_positions)
    board[position[0]][position[1]] = symbol

def play_game(mode):
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    symbols = ["X", "O"]
    random.shuffle(symbols)
    player_symbol, computer_symbol = symbols

    while True:
        if mode == "single":
            if player_symbol == "X":
                player_move(board, player_symbol)
                print_board(board)
                if check_winner(board):
                    print("Congratulations! You win!")
                    break
                if is_board_full(board):
                    print("It's a draw!")
                    break
                computer_move(board, computer_symbol)
                print("Computer's move:")
                print_board(board)
                if check_winner(board):
                    print("Computer wins!")
                    break
                if is_board_full(board):
                    print("It's a draw!")
                    break
            else:
                computer_move(board, computer_symbol)
                print("Computer's move:")
                print_board(board)
                if check_winner(board):
                    print("Computer wins!")
                    break
                if is_board_full(board):
                    print("It's a draw!")
                    break
                player_move(board, player_symbol)
                print_board(board)
                if check_winner(board):
                    print("Congratulations! You win!")
                    break
                if is_board_full(board):
                    print("It's a draw!")
                    break
        elif mode == "multi":
            player_move(board, player_symbol)
            print_board(board)
            if check_winner(board):
                print("Congratulations! You win!")
                break
            if is_board_full(board):
                print("It's a draw!")
                break
            player_symbol = "O" if player_symbol == "X" else "X"

if __name__ == "__main__":
    mode = input("Choose game mode (single/multi): ").lower()
    play_game(mode)

def lambda_handler(event, context):
    try:
        # Parse the request body
        request_body = json.loads(event['body'])
        
        # Extract the game mode from the request body
        mode = request_body.get('mode', 'single')  # Default to single player mode if mode is not provided
        
        # Implement the game logic based on the mode
        if mode == 'single':
            # Single player mode logic
            response = single_player_game()
        elif mode == 'multi':
            # Multiplayer mode logic
            response = multiplayer_game()
        else:
            # Invalid mode provided
            response = {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid game mode'})
            }
    except json.JSONDecodeError:
        # Error parsing request body
        response = {
            'statusCode': 400,
            'body': json.dumps({'message': 'Error parsing request body'})
        }
    except Exception as e:
        # Other unexpected errors
        response = {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
    
    # Format the response
    return {
        'statusCode': response['statusCode'],
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': response['body']
    }

def single_player_game():
    # Implement the single player game logic here
    pass

def multiplayer_game():
    # Implement the multiplayer game logic here
    pass

def print_board(board):
    # Helper function to print the game board
    pass

def check_winner(board):
    # Helper function to check if there's a winner
    pass

def is_board_full(board):
    # Helper function to check if the board is full
    pass

def get_empty_positions(board):
    # Helper function to get empty positions on the board
    pass

def player_move(board, symbol, position):
    # Helper function for player's move
    pass

def computer_move(board, symbol):
    # Helper function for computer's move
    pass
