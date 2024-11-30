import random
from .base import ColorSpace


class HSLColorSpace(ColorSpace):
    type = 'hsl'

    def random_color(self):
        return {
            "type": self.type,
            "hue": random.randint(0, 360),
            "saturation": random.randint(0, 100),
            "lightness": random.randint(0, 100)
        }
