from abc import ABC, abstractmethod


class ColorSpace(ABC):
    @property
    @abstractmethod
    def type(self):
        """Type of the color space, e.g., "rgb", "hsl"."""
        pass

    @abstractmethod
    def random_color(self):
        """Generate a random color in this color space."""
        pass
