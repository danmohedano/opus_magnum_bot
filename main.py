from bot import Board
import input


def main():
    board = Board()
    board_state = input.read_image('test.png')
    print('Board State read: ' + board_state)
    board.load(board_state)
    board.print()
    print("----------SOLUTION----------")
    board.backtrack()


if __name__ == '__main__':
    main()
