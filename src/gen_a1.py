#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zoltan Kuscsik
# Email: zoltan@s57.io
# License: MIT

# Generate an A1 size image with a grid of ArUco markers.
# The markers are numbered and the numbers are printed below the markers.

import cv2
import numpy as np

A1_WIDTH, A1_HEIGHT = 1684, 1189

TEXT_HEIGHT = 20
A1_HEIGHT += TEXT_HEIGHT * 9

image = np.ones((A1_HEIGHT, A1_WIDTH, 3), np.uint8) * 255

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

grid_size_x, grid_size_y = 16, 9

marker_size = min((A1_WIDTH // grid_size_x), (A1_HEIGHT // grid_size_y) - TEXT_HEIGHT)

for x in range(grid_size_x):
    for y in range(grid_size_y):
        marker_id = y * grid_size_x + x
        marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, 1)

        top_left_x = x * marker_size
        top_left_y = y * (marker_size + TEXT_HEIGHT)
        marker_image_bgr = cv2.cvtColor(marker_image, cv2.COLOR_GRAY2BGR)

        image[top_left_y:top_left_y + marker_size, top_left_x:top_left_x + marker_size] = marker_image_bgr

        text_position = (top_left_x, top_left_y + marker_size + TEXT_HEIGHT - 5)
        cv2.putText(image, str(marker_id), text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)

cv2.imwrite('img/aruco_grid_with_text.png', image)
