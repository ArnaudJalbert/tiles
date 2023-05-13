from PIL import Image, ImageDraw
from tiles_constants import *


def create_image():
    return Image.new(IMAGE_COLOR_SPACE, IMAGE_RESOLUTION, IMAGE_BG_COLOR)


def draw_line(image: Image, start: tuple, end: tuple, color=(0,0,0), width=10):
    draw = ImageDraw.Draw(image)
    draw.line((start, end), color, width)


if __name__ == '__main__':
    print("Tile Project")
    image = create_image()
    draw_line(image, (1,10), (50,50))
    image.save('image.png')
