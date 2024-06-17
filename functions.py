import os
from pathlib import Path
from PIL import Image
from settings import TILE_SIZE, TRANSPARENCY, BASE_DIR, WIDTH_PX, HEIGHT_PX


def set_transparency(image: Image, transparency: int):
    """
    Sets the transparency of the given image.
    :param image: PIL.Image
    :param transparency: int (0 to 255)
    :return: PIL.Image with transparency set
    """
    image = image.convert("RGBA")
    alpha = image.split()[3]
    alpha = alpha.point(lambda p: p * transparency / 255)
    image.putalpha(alpha)
    return image


def get_mosaic_number(path: str) -> int:
    """
    Get the last photo in the mosaic folder.
    :param path: str
    :return: int
    """
    photos = [int(file.split(".")[0].split("_")[-1]) for file in os.listdir(path) if file.endswith(".png")]
    return max(photos) + 1


def load_images(path: Path) -> list[Image]:
    """
    Load all images from the given path.
    :param path: str
    :return: list[Image]
    """
    images = []
    for path in path.iterdir():
        im = Image.open(path).resize((100, 100))  # Adjust tile size if needed
        images.append(im)
        print(f"Loaded {path}")
    return images


def get_mosaic(bg_im, shuffled_image_gen):
    for x in range(0, WIDTH_PX, TILE_SIZE):
        for y in range(0, HEIGHT_PX, TILE_SIZE):
            im = set_transparency(next(shuffled_image_gen), TRANSPARENCY)
            bg_im.paste(im, (x, y), im)
    print("Mosaic created")
    return bg_im


def get_output_path() -> Path:
    OUTPUT_IMAGE = os.path.join(BASE_DIR, f"mosaic_photo/mosaic/mosaic_{str(get_mosaic_number("mosaic"))}.png")
    output_path = Path(OUTPUT_IMAGE)
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    return output_path
