N_ROWS = 11
ROW_LENGTHS = [6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6]

N_ELEMENTS = 14

# Cardinal Elements
FIRE = 1
EARTH = 2
WATER = 3
WIND = 4

SALT = 5

# Opposition
LIFE = 6
DEATH = 7

# Metals
LEAD = 8
TIN = 9
IRON = 10
COPPER = 11
SILVER = 12
GOLD = 13

QUICKSILVER = 14

# Possible pairs for elimination of elements
PAIRS = {1: [1, 5, ],
         2: [2, 5, ],
         3: [3, 5, ],
         4: [4, 5, ],
         5: [1, 2, 3, 4, 5, ],
         6: [7, ],
         7: [6, ],
         8: [14, ],
         9: [14, ],
         10: [14, ],
         11: [14, ],
         12: [14, ],
         13: [],
         14: [8, 9, 10, 11, 12, ]}

# String shortcuts
LETTERS = {'f': 1,
           'e': 2,
           'w': 3,
           'a': 4,
           's': 5,
           'l': 6,
           'd': 7,
           'm': 8,
           't': 9,
           'i': 10,
           'c': 11,
           'p': 12,
           'g': 13,
           'q': 14,
           'X': 0
           }

LETTERS_INV = {0: 'X',
               1: 'f',
               2: 'e',
               3: 'w',
               4: 'a',
               5: 's',
               6: 'l',
               7: 'd',
               8: 'm',
               9: 't',
               10: 'i',
               11: 'c',
               12: 'p',
               13: 'g',
               14: 'q'}

NAMES = {1: 'Fire',
         2: 'Earth',
         3: 'Water',
         4: 'Wind',
         5: 'Salt',
         6: 'Life',
         7: 'Death',
         8: 'Lead',
         9: 'Tin',
         10: 'Iron',
         11: 'Copper',
         12: 'Silver',
         13: 'Gold',
         14: 'Quicksilver'
         }
