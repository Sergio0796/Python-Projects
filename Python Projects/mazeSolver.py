import time


class Maze():
    """A pathfinding problem"""

    def __init__(self, grid, location, path=[]):
        """Instances differ by their current agent locations"""

        self.grid = grid
        self.location = location
        self.path = path

    def display(self):
        """Print the maze, marking the current agent location"""

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('*', end='')
                else:
                    print(self.grid[r][c], end='')
            print()
        print()

    def moves(self):
        """Returns a list of possible moves given the current agent location"""
        location = self.location
        final = []
        row = location[0]
        col = location[1]
        if self.grid[row][col + 1] != "X":
            final.append("E")

        if self.grid[row][col - 1] != "X":
            final.append("W")

        if self.grid[row + 1][col] != "X":
            final.append("S")

        # Check if north is open
        if self.grid[row - 1][col] != "X":
            final.append("N")
        # print(final)  -Printing the final output list

        return final

    def neighbor(self, move):
        """Return another Maze instance with a move made"""
        location1 = self.location
        lpath = self.path + [move]

        row = location1[0]
        col = location1[1]
        nextMove = []
        if move == 'E':
            nextMove.append(row)
            nextMove.append(col + 1)

        if move == 'S':
            nextMove.append(row + 1)
            nextMove.append(col)
        if move == 'N':
            nextMove.append(row)
            nextMove.append(col - 1)
        if move == 'W':
            nextMove.append(row - 1)
            nextMove.append(col)
        return Maze(self.grid, tuple(nextMove), lpath)
        print(nextMove)


class Agent():
    """knows how to find the exit to a maze with BFS"""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal"""
        frontier = []
        frontier.append(maze)
        visited = [(1, 1)]  # set to keep track if already visited



        while frontier != 0:
            node = frontier.pop(0)
            for move in node.moves():
                view = node.neighbor(move)
                if view.location not in visited:
                    visited.append(view.location)
                    if view.location == goal.location:
                        return view.path
                    frontier.append(view)


def main():
    """Create a maze, solve it with bfs, and console animate"""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)
    maze.neighbor(maze)
    print(maze.moves())

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()


if __name__ == '__main__':
    main()