#!/usr/bin/python3
import sys

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        # Collecting solution
        solution = []
        for row in range(n):
            solution.append(''.join(board[row]))
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'  # Place queen
            solve_n_queens_util(board, col + 1, n, solutions)  # Recur
            board[i][col] = '.'  # Backtrack

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    print_solutions(solutions)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solve_n_queens(n)

if __name__ == "__main__":
    main()
