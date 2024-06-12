import streamlit as st
import numpy as np

st.title("Tic Tac Toe 5x5")

# Initialize the game board
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((5, 5))

if 'turn' not in st.session_state:
    st.session_state.turn = 1

def check_winner(board):
    # Check rows and columns
    for i in range(5):
        if np.all(board[i, :] == board[i, 0]) and board[i, 0] != 0:
            return board[i, 0]
        if np.all(board[:, i] == board[0, i]) and board[0, i] != 0:
            return board[0, i]
    # Check diagonals
    if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != 0:
        return board[0, 0]
    if np.all(np.fliplr(board).diagonal() == board[0, 4]) and board[0, 4] != 0:
        return board[0, 4]
    # Check for draw
    if not np.any(board == 0):
        return 0
    return None

def reset_game():
    st.session_state.board = np.zeros((5, 5))
    st.session_state.turn = 1

winner = check_winner(st.session_state.board)

if winner is not None:
    if winner == 0:
        st.write("It's a draw!")
    else:
        st.write(f"Player {int(winner)} wins!")
    if st.button("Play Again"):
        reset_game()
else:
    for i in range(5):
        cols = st.columns(5)
        for j in range(5):
            with cols[j]:
                if st.session_state.board[i, j] == 0:
                    if st.button(" ", key=f"{i}{j}"):
                        st.session_state.board[i, j] = st.session_state.turn
                        st.session_state.turn = 3 - st.session_state.turn
                else:
                    st.write("X" if st.session_state.board[i, j] == 1 else "O")

st.write(st.session_state.board)
