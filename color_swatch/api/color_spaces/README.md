# Color Spaces

A color space is a class that represents a different way of defining a color. E.g., rgb, hsl, etc.

Each color space implements a common abstract base class that can generate a random color in the given space.

## Add a new color space

Let's walk through adding a new color space.

Add a new file for your color space in `api/color_spaces`

```bash
touch api/color_spaces/foo.py
```

Add a new class that implements the ColorSpace abstract base class.

```python
# api/color_spaces/foo.py

from .base import ColorSpace

class FooColorSpace(ColorSpace):
    type = 'foo'
    
    def random_color(self):
        return {
            "type": self.type,
            # ...
        }

```

Register the new color space in `__init__.py` by adding it to the registered color spaces list.

```python
# api/color_spaces/__init__.py

from .base import ColorSpace
from .foo import FooColorSpace

# Register new color spaces here by adding to the list below
COLOR_SPACES: list[ColorSpace] = [
    FooColorSpace(),
    # More color spaces go here...
]
```

The new color space is now available in the API.

```bash
curl /api/colors
curl /api/colors/foo
```
