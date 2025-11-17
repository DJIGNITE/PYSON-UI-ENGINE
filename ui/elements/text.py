import pygame
from .base_element import BaseElement

class Text(BaseElement):
    def __init__(
        self,
        msg,
        font_size=30,
        color=(255, 255, 255),
        max_width=None,
        offset=(0, 0),
    ):
        """Initialize the text class using msg, font size, color, width, and 
        offset"""

        self.msg = msg
        self.font_size = font_size
        self.color = color
        self.offset = offset
        self.max_width = max_width

        self.font = pygame.font.SysFont(None, self.font_size)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.lines = []
        self.line_height = self.font.get_height()

        # Initial render
        self._render_text()


    def _render_text(self):
        """Wrap text (if max_width) and render surfaces."""

        if self.max_width:
            words = self.msg.split(" ")
            lines = []
            current_line = ""
            for word in words:
                test_line = current_line + (" " if current_line else "") + word
                if self.font.size(test_line)[0] <= self.max_width:
                    current_line = test_line
                else:
                    if current_line:
                        lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
        else:
            lines = self.msg.split("\n")

        self.lines = [self.font.render(line, True, self.color) for line in lines]

        width = max(line.get_width() for line in self.lines)
        height = sum(line.get_height() for line in self.lines)
        self.rect.size = (width, height)
        self.line_height = self.font.get_height()

    
    def move(self, pos):
        """Move the text box and keep it aligned."""

        self.rect.topleft = pos
        # No need to re-render unless max_width changes

    def resize(self, max_width):
        """Change max width and re-wrap text."""

        self.max_width = max_width
        self._render_text()

    def update_msg(self, new_msg):
        """Change text content and re-render."""

        self.msg = new_msg
        self._render_text()

    def draw(self, surface):
        """Draw the text to the screen."""
        
        y = self.rect.top
        for line in self.lines:
            surface.blit(line, (self.rect.left, y))
            y += self.line_height
