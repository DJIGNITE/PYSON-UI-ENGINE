# base_element.py

import pygame


class BaseElement:
    """Base class for all UI elements."""
    __slots__ = ("rect", "offset", "visible")

    def __init__(self, width=0, height=0, offset=(0, 0)):
        """Initialize the rect and offset and checks if element should be 
        visible."""
        self.rect = pygame.Rect(0, 0, width, height)
        self.offset = offset 
        self.visible = True   

    def measure(self):
        """ Return preferred size (width, height) of element.
        Child classes can override to compute size based on content."""

        return self.rect.width, self.rect.height

    def draw(self, surface):
        """Draw the element. Child classes must override."""
        raise NotImplementedError("Child class must implement draw(surface)")
        # raise NotImplementedError if not overridden

    def apply_offset(self):
        """Apply offset to rect position."""
        self.rect.x += self.offset[0]
        self.rect.y += self.offset[1]

    def __repr__(self):
        """Representation for debugging."""
        return f"<{self.__class__.__name__} rect={self.rect} offset={self.offset}>"
