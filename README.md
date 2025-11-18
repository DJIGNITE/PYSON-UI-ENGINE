####Just realized that this has been done. Ill still continue in my endeavors, just for practice

# PYSON-UI-ENGINE  
JSON-driven UI Engine for Pygame


# Description
Lightweight UI layout engine allowing users to create JSON driven screens. Gives user the freedom to describe containers, elements, offsets and offsets. The engine then takes care of the rest, drawing everything inside of your pygame application.


# Features:
- Define UI layout and elements in JSON
- Supports containers with vertical or horizontal spacing.
- Elements:
  - Text with optional wrapping
  - Clickable Buttons (minimally styled)
- Align Elements to:
  - Screen Edges
  - Other Elements
  - Inside Containers
- Easily Integration to existing Pygame projects


# Prerequistes
- Python 3
- Pygame
- Clone or add PYSON-UI-ENGINE to your project


# Installation
- Add this repository directly to your project root
- import the engine as a Module
  - from ui.layout.layout_engine import LayoutEngine

# JSON Keys -- Check out example.json file in repo
### screen: Global settings
  - width: Width of the application screen
  - height: Height of the application screen
  - bg_color: Background color of the application screen
  - title: Title of the application screen
### elements: UI element dictionary, keyed by name.
  - type: Defines the type of UI element to be placed (text or button currently)
  - msg: The text to be displayed either on the button or standalone
  -  text:
    - font_size : The size of the font to be used.
    - font_color: Color of the font to be used give as [r, g, b]
    - max_width: Optional key for setting the max width of a block of text for wrapping
    - align: Aligns the element to the container it is in. If no container, aligns to screen.
      - "top_left", "top_right", "bottom_right", "bottom_left", or "center"
    - align_to: Aligns the element to another element.
      - name: Name of the reference element for alignment
      -  position: Where the element will be place relative to the reference element.
        -  takes one of four positional values, "top", "bottom", "left", or "right"
    - offset: The amount the element will be offset from its alignment given as [x, y] 
  - Note: You can either choose align or align_to (not both)
### containers: UI container dictionary, keyed by name:
  - size: The size of the container given as [width, height]
  - align: Same as elements align key.
  - offset: same as elements offset key given as [x, y]
  - children: the list of elements that will be contained inside the container given as ["name_key", ...]
  - layout: Define the layout of the children in the container.
    - type: how will the elements be aligned inside the container. (vertical or horizontal)
    - spacing: How much space between each element inside the container
    - align_children: Where will the first element be place for alignment.
      - "left", "center", "right" for vertical container
      - "top", "center", "bottom" for horizontal container
    - vertical_align: Specific to vertical container. "top", "center", "bottom". Position the stack of elements in the container.
    - horizontal_align: Specific to horizontal container. "left", "right", "center". Position the row of elements in the container.
   
      
# Use -- check out example.py in repo
1. import pygame
2. import json
3. Import the LayoutEngine module
4. Load the file
5. Define the screen in terms of the json file
6. Define the engine and elements
7. Draw the elements to the screen




