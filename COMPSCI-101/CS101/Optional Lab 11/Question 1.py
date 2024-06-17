grid = "         "
player1 = "X"
player2 = "O"
print("Grid (before):", grid)


def play_turn(grid, player):
    grid_position = int(input("Enter the grid position you want to use (1 - 9): "))
    while (grid_position < 1 or grid_position > 9) and grid[grid_position - 1] != " ":
        if grid_position < 1 or grid_position > 9:
            print("Enter a valid grid position. Values should be between 1 and 9 inclusive")
            grid_position = int(input("Enter the grid position you want to use (1 - 9): "))
        elif grid[grid_position - 1] != " ":
            print("Grid position has been used. Choose a vacant grid position.")
            grid_position = int(input("Enter the grid position you want to use (1 - 9): "))

    grid = grid[:grid_position - 1] + player + grid[grid_position:]
    return grid



grid = play_turn(grid, player1)
print("Grid (after):", grid)