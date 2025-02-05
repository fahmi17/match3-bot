from flask import Flask, request, jsonify
import json
import random
from server.learning import QLearning

app = Flask(__name__)
q_agent = QLearning()

def find_best_move(board_state):
    best_move = None
    best_score = 0

    for row in range(len(board_state)):
        for col in range(len(board_state[row])):
            # Coba swap dengan tile sebelah kanan
            if col < len(board_state[row]) - 1:
                new_board = [row.copy() for row in board_state]
                new_board[row][col], new_board[row][col+1] = new_board[row][col+1], new_board[row][col]
                score = evaluate_board(new_board)
                if score > best_score:
                    best_score = score
                    best_move = {"x1": col, "y1": row, "x2": col+1, "y2": row}

            # Coba swap dengan tile bawah
            if row < len(board_state) - 1:
                new_board = [row.copy() for row in board_state]
                new_board[row][col], new_board[row+1][col] = new_board[row+1][col], new_board[row][col]
                score = evaluate_board(new_board)
                if score > best_score:
                    best_score = score
                    best_move = {"x1": col, "y1": row, "x2": col, "y2": row+1}

    return best_move if best_move else {"x1": 0, "y1": 0, "x2": 1, "y2": 0}  # Random move jika tidak ada yang bagus

def evaluate_board(board):
    score = 0
    for row in board:
        for i in range(len(row) - 2):
            if row[i] == row[i+1] == row[i+2]:
                score += 1
    return score

@app.route('/get_move', methods=['GET'])
def get_move():
    board_state_str = request.args.get("board_state")
    board_state = json.loads(board_state_str.replace("'", '\"'))  # Konversi string ke list

    move = q_agent.get_best_action(board_state)
    if move is None:
        move = find_best_move(board_state)

    return jsonify(move)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
