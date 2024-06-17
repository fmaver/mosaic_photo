# This python file is for setting up the configuration of the project.

import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

############ DEFINE THE PRINCIPAL PHOTO ############
PRINCIPAL_PHOTO_NAME = "principal.heic"
####################################################

# Define the path to the original image
ORIGINAL_IMAGE = os.path.join(BASE_DIR, f"mosaic_photo/photos/principal/{PRINCIPAL_PHOTO_NAME}")

############### DEFINE THE TILE PHOTO ##############
TILE_PHOTOS_PATH = "photos/tile/franyguadi"
####################################################

# Define the path to the images
IMAGES_DIR = Path(os.path.join(BASE_DIR, f"mosaic_photo/{TILE_PHOTOS_PATH}"))

# Define the DPI of the output image
DPI = 300

# Define the dimensions of the output image in cm
WIDTH_CM = 30
HEIGHT_CM = 40

# Define the conversion factor from cm to inch
CM_TO_INCH = 2.54

# Define the dimensions of the output image in pixels
WIDTH_PX = int(WIDTH_CM * DPI / CM_TO_INCH)
HEIGHT_PX = int(HEIGHT_CM * DPI / CM_TO_INCH)

# Define the tile size
TILE_SIZE = 100

# Define the transparency of the tiles
TRANSPARENCY = 100

# Define the number of tiles to generate
NUM_TILES = 1000
