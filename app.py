
import streamlit as st

st.set_page_config(page_title="🎮 Tic Tac Toe", layout="centered")

st.title("🎮 Tic Tac Toe")
st.write("Play a two-player game of Tic Tac Toe!")

# Initialize the game
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# Check for winner
def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    if all(cell != "" for cell in board):
        return "Draw"
    return None

# Create 3x3 buttons
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i):
            if st.session_state.board[i] == "" and st.session_state.winner is None:
                st.session_state.board[i] = st.session_state.turn
                st.session_state.winner = check_winner(st.session_state.board)
                st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("It's a draw!")
    else:
        st.success(f"{st.session_state.winner} wins!")
    if st.button("Play Again"):
        st.session_state.board = [""] * 9
        st.session_state.turn = "X"
        st.session_state.winner = None
else:
    st.write(f"Turn: **{st.session_state.turn}**")
