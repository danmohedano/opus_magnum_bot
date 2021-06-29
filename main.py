from bot import Board


def main():
    board = Board()
    board.load("      e  w   fwwaqffewsfe fasa lewweqlcw  wadgqts    a pa m   lqsalfd   efqe    die   adf  ")
    board.print()
    print("~~~~~~~~~~SOLUTION~~~~~~~~~~")
    board.backtrack()


if __name__ == '__main__':
    main()
