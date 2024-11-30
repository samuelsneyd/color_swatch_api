import random
from .base import ColorSpace
from .rgb import RGBColorSpace
from .hsl import HSLColorSpace

COLOR_SPACES = [RGBColorSpace(), HSLColorSpace()]


def get_random_color_space():
    """Returns a random color space"""
    return random.choice(COLOR_SPACES)


def get_random_color_and_space():
    """Returns a random color from a random color space."""
    return random.choice(COLOR_SPACES).random_color()


def get_color_space(color_space_type: str):
    """Returns a color space by type, e.g., "rbg", "hsl"."""
    for color_space in COLOR_SPACES:
        if color_space.type == color_space_type:
            return color_space

