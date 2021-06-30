# Opus Magnum Bot
Bot to play Opus Magnum's solitaire minigame Sigmar's Garden. It uses backtracking to find the solution and comparison between images using Structural Similarity Index ([SSIM](https://en.wikipedia.org/wiki/Structural_similarity)) to detect from an image the state of the board.

The program utilizes the `opencv-python` and `numpy` libraries to manage the images and `scikit-image` to calculate SSIM. 
## Rules
![om_rules](https://user-images.githubusercontent.com/43313293/123773336-e44b4c00-d8cc-11eb-8a3f-1066120a7ba6.png)


## Usage
The user can input the state of the board through a single string describing the contents of every row starting from the top and using the following abbreviations for each element:

![help](https://user-images.githubusercontent.com/43313293/123773432-f331fe80-d8cc-11eb-9b2f-7cfb43395859.png)

The preferred (and faster) method is to do a screenshot of the game's window in Fullscreen mode and input that to the program. 

## Example output
    Processing image...
    Board State read: XXXXcXwleesfXXaeXffwXXssXaXXpXXaXawaeqqfXetXegfXdqXwddfafqXmXXiXXqXlwXXalfXewXXasdwlwXeXXXX
          [0, 0, 0, 0, 11, 0]
         [3, 6, 2, 2, 5, 1, 0]
        [0, 4, 2, 0, 1, 1, 3, 0]
       [0, 5, 5, 0, 4, 0, 0, 12, 0]
      [0, 4, 0, 4, 3, 4, 2, 14, 14, 1]
     [0, 2, 9, 0, 2, 13, 1, 0, 7, 14, 0]
      [3, 7, 7, 1, 4, 1, 14, 0, 8, 0]
       [0, 10, 0, 0, 14, 0, 6, 3, 0]
        [0, 4, 6, 1, 0, 2, 3, 0]
         [0, 4, 5, 7, 3, 6, 3]
          [0, 2, 0, 0, 0, 0]
    Element  1 ( Fire ):  [(1, 5), (2, 4), (2, 5), (4, 9), (5, 6), (6, 3), (6, 5), (8, 3)]
    Element  2 ( Earth ):  [(1, 2), (1, 3), (2, 2), (4, 6), (5, 1), (5, 4), (8, 5), (10, 1)]
    Element  3 ( Water ):  [(1, 0), (2, 6), (4, 4), (6, 0), (7, 7), (8, 6), (9, 4), (9, 6)]
    Element  4 ( Wind ):  [(2, 1), (3, 4), (4, 1), (4, 3), (4, 5), (6, 4), (8, 1), (9, 1)]
    Element  5 ( Salt ):  [(1, 4), (3, 1), (3, 2), (9, 2)]
    Element  6 ( Life ):  [(1, 1), (7, 6), (8, 2), (9, 5)]
    Element  7 ( Death ):  [(5, 8), (6, 1), (6, 2), (9, 3)]
    Element  8 ( Lead ):  [(6, 8)]
    Element  9 ( Tin ):  [(5, 2)]
    Element  10 ( Iron ):  [(7, 1)]
    Element  11 ( Copper ):  [(0, 4)]
    Element  12 ( Silver ):  [(3, 7)]
    Element  13 ( Gold ):  [(5, 5)]
    Element  14 ( Quicksilver ):  [(4, 7), (4, 8), (5, 9), (6, 6), (7, 4)]
    Accessible Elements:
    ( 0 , 4 )[ 11 ]
    ( 1 , 0 )[ 3 ]
    ( 4 , 9 )[ 1 ]
    ( 6 , 0 )[ 3 ]
    ( 9 , 6 )[ 3 ]
    ( 10 , 1 )[ 2 ]
    ----------SOLUTION----------
    [ Gold ]( 6 , 6 )
    [ Wind ]( 4 , 5 ) ---- [ Wind ]( 5 , 6 )
    [ Fire ]( 6 , 7 ) ---- [ Fire ]( 3 , 6 )
    [ Water ]( 3 , 7 ) ---- [ Water ]( 5 , 5 )
    [ Earth ]( 5 , 7 ) ---- [ Earth ]( 6 , 5 )
    [ Fire ]( 7 , 6 ) ---- [ Fire ]( 3 , 5 )
    [ Wind ]( 5 , 4 ) ---- [ Wind ]( 7 , 5 )
    [ Fire ]( 2 , 6 ) ---- [ Salt ]( 2 , 5 )
    [ Silver ]( 4 , 8 ) ---- [ Quicksilver ]( 8 , 5 )
    [ Fire ]( 9 , 4 ) ---- [ Fire ]( 7 , 4 )
    [ Copper ]( 1 , 5 ) ---- [ Quicksilver ]( 7 , 7 )
    [ Life ]( 8 , 7 ) ---- [ Death ]( 7 , 3 )
    [ Earth ]( 2 , 4 ) ---- [ Earth ]( 9 , 6 )
    [ Iron ]( 8 , 2 ) ---- [ Quicksilver ]( 5 , 8 )
    [ Life ]( 9 , 3 ) ---- [ Death ]( 6 , 9 )
    [ Tin ]( 6 , 3 ) ---- [ Quicksilver ]( 5 , 9 )
    [ Quicksilver ]( 6 , 10 ) ---- [ Lead ]( 7 , 9 )
    [ Water ]( 10 , 5 ) ---- [ Water ]( 8 , 8 )
    [ Earth ]( 2 , 3 ) ---- [ Earth ]( 3 , 3 )
    [ Salt ]( 4 , 3 ) ---- [ Water ]( 9 , 7 )
    [ Death ]( 10 , 4 ) ---- [ Life ]( 10 , 6 )
    [ Wind ]( 3 , 2 ) ---- [ Wind ]( 9 , 2 )
    [ Water ]( 10 , 7 ) ---- [ Salt ]( 4 , 2 )
    [ Fire ]( 5 , 10 ) ---- [ Salt ]( 10 , 3 )
    [ Wind ]( 10 , 2 ) ---- [ Wind ]( 5 , 2 )
    [ Life ]( 2 , 2 ) ---- [ Death ]( 7 , 2 )
    [ Earth ]( 11 , 2 ) ---- [ Earth ]( 6 , 2 )
    [ Water ]( 2 , 1 ) ---- [ Water ]( 7 , 1 )