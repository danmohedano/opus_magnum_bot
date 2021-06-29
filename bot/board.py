from .constants import ROW_LENGTHS, N_ROWS, N_ELEMENTS, LEAD, GOLD, PAIRS, SILVER, QUICKSILVER, LETTERS, NAMES
import numpy as np


def neighbours(row, column):
    """
    Auxiliary function to calculate the neighbours to a given position
    :param row:
    :param column:
    :return: list of positions
    """
    if row <= np.floor(N_ROWS / 2):
        # Top half
        top_column = column - 1
    else:
        # Bottom half
        top_column = column

    if row < np.floor(N_ROWS / 2):
        # Top half
        bottom_column = column
    else:
        # Bottom half
        bottom_column = column - 1

    return [(row, column - 1),
            (row - 1, top_column),
            (row - 1, top_column + 1),
            (row, column + 1),
            (row + 1, bottom_column + 1),
            (row + 1, bottom_column)]


def check_adjacent(a):
    """
    Check if three empty slots are adjacent
    :param a: array
    :return: True or False
    """
    counter = 0
    for i in a:
        if i:
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0

    # Do two loops as the structure is circular
    for i in a:
        if i:
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0

    return False


class Board:
    def __init__(self):
        """
        Initialize the empty board.
        """
        # Board to store which elements are placed in each position
        self.board = []
        for i in ROW_LENGTHS:
            self.board.append([0] * i)

        # Position of all the different elements
        self.element_positions = {}
        for i in range(1, N_ELEMENTS + 1):
            self.element_positions[i] = []

        # Position of the currently accessible elements
        self.accessible_elements = []

        # Current status of the metal elimination
        self.metal_status = 0

    def print(self):
        """
        Print status of board
        :return: None
        """
        for row in self.board:
            padding = N_ROWS - len(row)
            addon = " " * padding
            print(addon, row)

        for i in range(1, len(self.element_positions) + 1):
            print("Element ", i, "(", NAMES[i], "): ", self.element_positions[i])

        print("Accessible Elements:")
        for row, column in self.accessible_elements:
            print("(", row, ",", column, ")[", self.board[row][column], "]")

    def load(self, new_board):
        """
        Load a new board
        :param new_board: new board to load in string format
        :return: None
        """
        counter = 0
        for i in range(N_ROWS):
            for ii in range(ROW_LENGTHS[i]):
                self.board[i][ii] = LETTERS[new_board[counter]]
                counter += 1

        for i in range(N_ROWS):
            for ii in range(ROW_LENGTHS[i]):
                # For each element in the board, save its position
                # and check if it is accesible
                if self.board[i][ii] != 0:
                    el = self.board[i][ii]

                    if self.accessible(i, ii):
                        self.accessible_elements.append((i, ii))

                    self.element_positions[el].append((i, ii))

    def accessible(self, row, column):
        """
        Calculate if an element is accesible or not
        An element is accesible if it has 3 empty adjacent
        slots surrounding it
        :param row: position of element
        :param column: position of element
        :return: True or False
        """
        empty = []

        positions = neighbours(row, column)

        for x, y in positions:
            if self.is_empty(x, y):
                empty.append(1)
            else:
                empty.append(0)

        if check_adjacent(empty):
            return True
        else:
            return False

    def is_empty(self, row, column):
        """
        See if a position is empty or not
        :param row: position
        :param column: position
        :return: True or False
        """
        if row < 0 or row >= N_ROWS:
            return True
        if column < 0 or column >= ROW_LENGTHS[row]:
            return True
        if self.board[row][column] == 0:
            return True
        else:
            return False

    def backtrack(self):
        """
        Backtracking function to solve the puzzle
        :return: True or False depending if a result is found
        """
        possibilities = self.possible_moves()
        if not possibilities:
            if self.check_win():
                return True
            else:
                return False

        for pos1, pos2 in possibilities:
            # Save information to undo move
            element1 = self.board[pos1[0]][pos1[1]]
            element2 = None
            if pos2:
                element2 = self.board[pos2[0]][pos2[1]]

            # Do move and keep solving
            self.move(element1, pos1, element2, pos2)
            if self.backtrack():
                if pos2:
                    print("[", NAMES[element1], "](", pos1[0] + 1, ",", pos1[1] + 1, ")",
                          "----",
                          "[", NAMES[element2], "](", pos2[0] + 1, ",", pos2[1] + 1, ")")
                else:
                    print("[", NAMES[element1], "](", pos1[0] + 1, ",", pos1[1] + 1, ")")
                return True

            # Undo and backtrack
            self.unmove(element1, pos1, element2, pos2)

        return False

    def check_win(self):
        """
        Check for a win (no elements in the board)
        :return: True or False
        """
        for i in self.element_positions:
            if len(self.element_positions[i]) != 0:
                return False

        return True

    def move(self, element1, pos1, element2, pos2):
        """
        Updates the information of the table after a move has been done
        :param element1: type of element 1
        :param pos1: position of element 1
        :param element2: type of element 2
        :param pos2: position of element 2
        :return: None
        """
        # Update board (leave empty space)
        self.board[pos1[0]][pos1[1]] = 0
        if pos2:
            self.board[pos2[0]][pos2[1]] = 0

        # Remove the positions from the element_positions dictionary
        self.element_positions[element1].remove(pos1)
        if pos2:
            self.element_positions[element2].remove(pos2)

        # Remove the positions from the accessible elements list
        self.accessible_elements.remove(pos1)
        if pos2:
            self.accessible_elements.remove(pos2)

        # Update metal status if necessary
        if element1 == LEAD + self.metal_status or \
                element2 == LEAD + self.metal_status:
            self.metal_status += 1

        # Calculate new accessible elements
        neighbours1 = neighbours(pos1[0], pos1[1])
        for row, column in neighbours1:
            if not self.is_empty(row, column) and \
                    self.accessible(row, column):
                if (row, column) not in self.accessible_elements:
                    self.accessible_elements.append((row, column))

        if pos2:
            neighbours2 = neighbours(pos2[0], pos2[1])
            for row, column in neighbours2:
                if not self.is_empty(row, column) and \
                        self.accessible(row, column):
                    if (row, column) not in self.accessible_elements:
                        self.accessible_elements.append((row, column))

    def unmove(self, element1, pos1, element2, pos2):
        """
        Undo a move
        :param element1: type of element 1
        :param pos1: position of element 1
        :param element2: type of element 2
        :param pos2: position of element 2
        :return: None
        """
        # Update board
        self.board[pos1[0]][pos1[1]] = element1
        if pos2:
            self.board[pos2[0]][pos2[1]] = element2

        # Add the positions to the element_positions dictionary
        self.element_positions[element1].append(pos1)
        if pos2:
            self.element_positions[element2].append(pos2)

        # Return the positions to the accessible elements list
        self.accessible_elements.append(pos1)
        if pos2:
            self.accessible_elements.append(pos2)

        # Update metal status if necessary
        if element1 == LEAD + self.metal_status - 1 or \
                element2 == LEAD + self.metal_status - 1:
            self.metal_status -= 1

        # Recalculate accessible elements
        neighbours1 = neighbours(pos1[0], pos1[1])
        for row, column in neighbours1:
            if not self.is_empty(row, column) and \
                    not self.accessible(row, column):
                if (row, column) in self.accessible_elements:
                    self.accessible_elements.remove((row, column))

        if pos2:
            neighbours2 = neighbours(pos2[0], pos2[1])
            for row, column in neighbours2:
                if not self.is_empty(row, column) and \
                        not self.accessible(row, column):
                    if (row, column) in self.accessible_elements:
                        self.accessible_elements.remove((row, column))

    def possible_moves(self):
        """
        Taking into account the accessible elements, the possible moves are
        calculated
        :return: list of moves of the form (position, position)
        """
        moves = []
        for row, column in self.accessible_elements:
            # Check if gold can be deleted
            element = self.board[row][column]
            if element == GOLD and self.metal_status == GOLD - LEAD:
                moves.append(((row, column), None))
            elif element < LEAD or element > GOLD or \
                    element == LEAD + self.metal_status:
                # Check if this element can be paired with any other
                # accessible element
                for row2, column2 in self.accessible_elements:
                    if row != row2 or column != column2:
                        if self.board[row2][column2] in PAIRS[element] and \
                                ((row2, column2), (row, column)) not in moves:
                            if element == QUICKSILVER:
                                if self.board[row2][column2] == LEAD + self.metal_status:
                                    moves.append(((row, column), (row2, column2)))
                            else:
                                moves.append(((row, column), (row2, column2)))

        return moves
