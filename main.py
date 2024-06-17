from pathlib import Path
from itertools import cycle
from random import shuffle

from pillow_heif import register_heif_opener
from PIL import Image

from functions import load_images, get_mosaic, get_output_path
from settings import ORIGINAL_IMAGE, CM_TO_INCH, DPI, WIDTH_CM, HEIGHT_CM, IMAGES_DIR

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transparency = 100  # Set the transparency level (0-255)

    register_heif_opener()
    ref_im = Image.open(ORIGINAL_IMAGE)

    width_px = int(WIDTH_CM * DPI / CM_TO_INCH)
    height_px = int(HEIGHT_CM * DPI / CM_TO_INCH)
    # width_px = 2232
    # height_px = 3968

    ref_im = ref_im.resize((width_px, height_px))
    bg_im = ref_im.resize((width_px, height_px))  # original image with the required size

    images = load_images(IMAGES_DIR)

    def shuffled_images(images: list[Image]):

        last_image = None
        while True:
            shuffle(images)
            for image in images:
                if image != last_image:
                    yield image
                    last_image = image
                else:
                    # If the same image, pick another one (since the list is shuffled, this is rare)
                    available_images = [img for img in images if img != last_image]
                    if available_images:
                        image = available_images[0]
                        yield image
                        last_image = image

    shuffled_image_gen = shuffled_images(images)

    pixels = ref_im.load()
    mosaic = get_mosaic(bg_im, shuffled_image_gen)

    output_path = get_output_path()
    mosaic.save(output_path)
    print(f"Saved mosaic to {output_path}")


