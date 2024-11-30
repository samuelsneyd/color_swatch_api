import random
from .base import ColorSpace


class RGBColorSpace(ColorSpace):
    type = 'rgb'

    def random_color(self):
        return {
            "type": self.type,
            "red": random.randint(0, 255),
            "green": random.randint(0, 255),
            "blue": random.randint(0, 255),
        }
