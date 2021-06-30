import cv2.cv2 as cv2
import os
from skimage.metrics import structural_similarity as ssim
from bot.constants import N_ROWS, ROW_LENGTHS, N_ELEMENTS, LETTERS_INV
from .constants import *


def read_image(img_name):
    """
    Function to read state of the board from image
    :param img_name: name of the image file
    :return: string containing the state of the board
    """
    # Read image and crop
    image = cv2.imread(img_name)
    image = image[180:880, 800:1650]

    # Show image for reference
    cv2.imshow('image', image)
    cv2.waitKey(0)

    # Extract the individual cells from the image
    print('Processing image...')
    cells = []
    vertical = INITIAL_V
    horizontal = INITIAL_H
    for i in range(N_ROWS):
        for ii in range(ROW_LENGTHS[i]):
            # Read cell
            cell = image[vertical:vertical+CELL_DIM, horizontal:horizontal+CELL_DIM]
            cells.append(cell)

            # Update horizontal variable for next cell in the row
            horizontal += NEXT_CELL_DISTANCE

        # Update both vertical and horizontal variables for the next row
        # Horizontal will need to be reset to the start of the row
        vertical += NEXT_ROW_DISTANCE_V
        horizontal -= ROW_LENGTHS[i] * NEXT_CELL_DISTANCE
        if i < (N_ROWS // 2):
            # First half of rows progressively start more to the left
            horizontal -= NEXT_ROW_DISTANCE_H
        else:
            # Second half progressively start more to the right
            horizontal += NEXT_ROW_DISTANCE_H

    # Compare each cell and find the element using Structural Similarity Index
    board_string = ''
    for i in cells:
        max_ssim = -1
        max_ele = -1
        for ele in range(2 * N_ELEMENTS + 1):
            img_b = cv2.imread(os.path.join('input', 'elements', '{}.png'.format(ele)))
            similarity = ssim(i, img_b, multichannel=True)
            if similarity > max_ssim:
                max_ssim = similarity
                max_ele = ele

        if max_ele % 2:
            max_ele += 1
        board_string += LETTERS_INV[max_ele / 2]

    return board_string
