# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 2/13/2024
# Description:

def row_puzzle(row, pos=0, visited=None):
    # Initialize visited set with default argument trick to avoid mutable default argument
    if visited is None:
        visited = set()

    # Base case: if current position is the rightmost square
    if pos == len(row) - 1:
        return True

    # If the position is already visited or out of bounds, return False to avoid infinite loops
    if pos in visited or pos < 0 or pos >= len(row):
        return False

    # Add current position to visited to avoid revisiting
    visited.add(pos)

    # Calculate new positions for potential moves
    move_value = row[pos]
    left_pos = pos - move_value
    right_pos = pos + move_value

    # Recursively check both left and right moves
    # Use set(visited) to create a copy of visited for each recursive call to avoid shared state
    return row_puzzle(row, left_pos, set(visited)) or row_puzzle(row, right_pos, set(visited))
