from abc import ABC, abstractmethod


class ColorSpace(ABC):
    @property
    @abstractmethod
    def type(self) -> str:
        """Type of the color space, e.g., "rgb", "hsl"."""
        pass

    @abstractmethod
    def random_color(self) -> dict:
        """Generate a random color in this color space."""
        pass
