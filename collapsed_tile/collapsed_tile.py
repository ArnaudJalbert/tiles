from PIL import Image, ImageDraw
from abc import abstractmethod


# image settings
IMAGE_COLOR_SPACE = "RGB"
IMAGE_RESOLUTION = (1000, 1000)
IMAGE_BG_COLOR = (255, 255, 255)

# border offset
BORDER_OFFSET = 20
TOTAL_LOOPS = 23


class Drawable(object):
    def __init__(self, image, name) -> None:
        self._image = image
        self._name = name

    @property
    def image(self):
        return self._image

    @property
    def name(self):
        return self._name

    @staticmethod
    def draw_line(image: Image, start: tuple, end: tuple, color=(0, 0, 0), width=10):
        draw = ImageDraw.Draw(image)
        draw.line((start, end), color, width)
        return end

    @staticmethod
    def create_image() -> Image:
        return Image.new(IMAGE_COLOR_SPACE, IMAGE_RESOLUTION, IMAGE_BG_COLOR)

    def save_image(self):
        image.save(".".join([self.name, "png"]))

    @abstractmethod
    def draw(self):
        pass


class CollapsedTile(Drawable):
    def __init__(
        self,
        image: Image,
        name: str,
        start_coordinate: tuple,
        offset=20,
        notch=20,
        loops=25,
    ) -> None:
        super(CollapsedTile, self).__init__(image, name)
        self.start_coordinate = start_coordinate
        self.offset = offset
        self.notch = notch
        self.loops = loops

    def draw(self):
        # starting coordinate
        coordinate = self.start_coordinate
        offset = self.offset

        for _square in range(self.loops):
            # left top corner to left bottom corner
            coordinate = self.draw_line(
                image,
                coordinate,
                (offset, IMAGE_RESOLUTION[1] - offset),
            )

            # left bottom corner to right bottom corner
            coordinate = self.draw_line(
                image,
                coordinate,
                (IMAGE_RESOLUTION[0] - offset, IMAGE_RESOLUTION[1] - offset),
            )

            # right bottom corner to top right corner
            coordinate = self.draw_line(
                image,
                coordinate,
                (IMAGE_RESOLUTION[1] - offset, offset),
            )

            # right bottom corner to top right corner
            coordinate = self.draw_line(
                image,
                coordinate,
                (offset + self.notch, offset),
            )

            offset += self.notch


if __name__ == "__main__":
    name = "animated_collapsed_tile_{}_v001"

    # first loop inwards
    for x in range(TOTAL_LOOPS):
        current_loop = x
        image = Drawable.create_image()

        collapsed_tile = CollapsedTile(
            image,
            name.format(x),
            (BORDER_OFFSET, BORDER_OFFSET),
            offset=30,
            loops=current_loop,
        )

        collapsed_tile.draw()

        collapsed_tile.save_image()

    for x in range(23):
        current_loop = 23 - x
        image = Drawable.create_image()

        collapsed_tile = CollapsedTile(
            image,
            name.format(x + 23),
            (BORDER_OFFSET, BORDER_OFFSET),
            offset=30,
            loops=current_loop,
        )

        collapsed_tile.draw()

        collapsed_tile.save_image()
