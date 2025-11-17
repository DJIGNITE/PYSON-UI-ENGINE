import pygame
from .base_element import BaseElement

class Button(BaseElement):
    def __init__(
        self,
        msg,
        size=(200, 50),
        font_size=40,
        bg_color=(0, 0, 0),
        text_color=(50, 200, 50),
        offset=(0, 0),
        initial_pos=None
    ):
        """Initialize all attributs of a button given a message, size,
        font size, background color, text color, offset, and initial
        position."""

        self.msg = msg
        self.size = size
        self.font_size = font_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.offset = offset
        self.clickable = True

        # define the rect based on the size param
        self.rect = pygame.Rect(0, 0, *size)

        if initial_pos:
            # places the rect at the initial position
            self.rect.topleft = initial_pos  

        self.font = pygame.font.SysFont(None, self.font_size)
        self.msg_surfaces = []
        self.msg_rects = []

        # make sure the text is rendered on the button
        self._render_text()

    def _render_text(self):
        """Render text after spliting them into lines using \n"""

        lines = self.msg.split("\n")
        line_height = self.font.get_height()
        total_height = line_height * len(lines)

        self.msg_surfaces = []
        self.msg_rects = []

        y = self.rect.top + (self.rect.height - total_height) // 2
        for line in lines:
            surf = self.font.render(line.strip(), True, self.text_color)
            rect = surf.get_rect(center=(self.rect.centerx, y + line_height//2))
            self.msg_surfaces.append(surf)
            self.msg_rects.append(rect)
            y += line_height

    def move(self, pos):
        """Move the button rect and update text positions."""

        self.rect.topleft = pos
        self._render_text()

    def draw(self, surface):
        """Draw the button to the screen."""
        
        pygame.draw.rect(surface, self.bg_color, self.rect)
        pygame.draw.rect(surface, self.text_color, self.rect, width=3)
        for surf, rect in zip(self.msg_surfaces, self.msg_rects):
            surface.blit(surf, rect)
