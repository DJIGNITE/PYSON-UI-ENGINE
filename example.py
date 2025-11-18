# standard library imports
import json
from pathlib import Path
import sys

# third party imports
import pygame

# import LayoutEngine
from ui.layout.layout_engine import LayoutEngine

class ExampleScreen:
    """Pygame screen driven by a json layout."""
    def __init__(self, layout_file="example.json"):
        """Initialize the screen using example.json"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.show = True

        # set layout_file as a Path to the file
        self.layout_file = Path(layout_file)

        # Load example.json
        self.config = self.load_layout()

        # create window and UI elements
        self.load_elements()

    def load_layout(self):
        """Load the layout from file example.json."""
        with open(self.layout_file) as ex_json:
            return json.load(ex_json)
        
    def load_elements(self):
        """Initialize the elements from the json file."""

        # initialize the screen
        screen_cfg = self.config["screen"]
        self.screen = pygame.display.set_mode((screen_cfg["width"], screen_cfg["height"]))
        pygame.display.set_caption(screen_cfg["title"])
        self.bg_color = tuple(screen_cfg.get("bg_color", [0, 0, 0]))

        # set the layout engine to take the screen as the canvas
        self.layout_engine = LayoutEngine(self.screen)
        self.ui_elements = self.layout_engine.load(self.config)

    def run(self):
        """Main screen loop."""
        while self.show:
            self._check_events()
            self.draw()
            self.clock.tick(60)

    def draw(self):
        """Draw the screen."""
        self.screen.fill(self.bg_color)


        # OPTIONAL
        # draw container outlines
        for ctr in self.layout_engine.containers.values():
            pygame.draw.rect(self.screen, (50, 50, 50), ctr["rect"], width=3)

        # draw elements
        for el in self.ui_elements.values():
            el.draw(self.screen)

        pygame.display.flip()

    def _check_events(self):
        """Check pygame events for input."""

        # enable window exit button 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ = "__main__":
    ExampleScreen().run()

        
        

    
