import copy
import time
from Queue import PriorityQueue

class Puzzle():
    """A sliding-block puzzle."""

    def __init__(self, grid):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number)
            print
        print

    def moves(self):
        """Return a list of possible moves given the current configuration."""

        final = []

        if self.grid[row + 1] != 3:
            final.append("S")
        if self.grid[row - 1] != 3:
            final.append("N")
        if self.grid[row][number + 1] != 3:
            final.append("E")
        if self.grid[row][number - 1] != 3:
            final.append("W")

        return final


    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        nextMove = []
        if move == 'E':
            nextMove.append(row)
            nextMove.append(col + 1)

        if move == 'S':
            nextMove.append(row + 1)
            nextMove.append(col)
        if move == 'N':
            nextMove.append(row-1)
            nextMove.append(number)
        if move == 'W':
            nextMove.append(row)
            nextMove.append(number-1)
        return Puzzle(tuple(nextMove))
    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        misplaced = 0
        distance = 0
        for i in range(9):
            if goal[i] != self.puzzle[i]:
                misplaced += 1
        for i in goal:
            distance += math.fabs(goal.index(i) - self.puzzle.index(i))
        total = distance + misplaced

        goal.append(total)
        return goal



class Agent():
    """Knows how to solve a sliding-block puzzle with A* search."""

    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
    finished = []
    frontier = PriorityQueue()
    puzzle = []             #starting list
    puzzle = puzzle.h(goal)
    frontier.append(puzzle)

    while frontier != 0 :
        frontier.heap(0)
        if frontier[0] == goal:
            break
        else: finish.append(frontier[0])
        for move in frontier:



    def main():
        """Create a puzzle, solve it with A*, and console-animate."""

        puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
        puzzle.display()

        agent = Agent()
        goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
        path = agent.astar(puzzle, goal)

    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()

    if __name__ == '__main__':
        main()