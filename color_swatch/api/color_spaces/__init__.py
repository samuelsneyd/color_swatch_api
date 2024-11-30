import random
from .base import ColorSpace
from .rgb import RGBColorSpace
from .hsl import HSLColorSpace

# Register new color spaces here by adding to the list below
COLOR_SPACES: list[ColorSpace] = [RGBColorSpace(), HSLColorSpace()]


def get_random_color_space() -> ColorSpace:
    """Returns a random color space."""
    return random.choice(COLOR_SPACES)


def get_random_color_and_space() -> dict:
    """Returns a random color from a random color space."""
    return random.choice(COLOR_SPACES).random_color()


def get_color_space(color_space_type: str) -> ColorSpace | None:
    """Returns a color space by type, e.g., "rbg", "hsl", or none if not found."""
    for color_space in COLOR_SPACES:
        if color_space.type == color_space_type:
            return color_space

    return None
