import pygame
from .container_layout import ContainerLayout
from ..elements.button import Button
from ..elements.text import Text

class LayoutEngine:
    def __init__(self, screen):
        """Initialize elements, containers, and Layouts"""

        self.screen = screen
        self.elements = {}
        self.containers = {}
        self.container_layout = ContainerLayout()

    def load(self, config):
        """Load elements,containers and places container children."""

        self._create_containers(config.get("containers", {}))
        self._create_elements(config.get("elements", {}))
        self._place_container_children()
        return self.elements

    
    def _create_containers(self, containers_data):
        """Creates containers defined inside json file."""

        for cname, data in containers_data.items():
            width, height = data["size"]
            rect = pygame.Rect(0, 0, width, height)
            ox, oy = data.get("offset", [0, 0])
            if "align" in data:
                self._align_to_screen(rect, data["align"], ox, oy)
            else:
                rect.topleft = (ox, oy)
            self.containers[cname] = {
                "type": "container",
                "rect": rect,
                "children": data.get("children", []),
                "layout": data.get("layout", {}),
                "offset": [ox, oy],
            }

    def _create_elements(self, elements_data):
        """Create elemnets defined in json file."""

        for name, data in elements_data.items():
            el_type = data["type"]
            offset = data.get("offset", [0, 0])
            initial_pos = self._calculate_initial_position(data)

            if el_type == "button":
                # create buttons.
                el = Button(
                    msg=data["msg"],
                    size=data.get("size", [200,50]),
                    font_size=data.get("font_size", 40),
                    bg_color=tuple(data.get("bg_color", [0,0,0])),
                    text_color=tuple(data.get("text_color", [50,200,50])),
                    offset=offset,
                    initial_pos=initial_pos
                )
            elif el_type == "text":
                # create text
                el = Text(
                    msg=data["msg"],
                    font_size=data.get("font_size", 30),
                    color=tuple(data.get("font_color", [255,255,255])),
                    max_width=data.get("max_width"),
                    offset=offset
                )
                if initial_pos:
                    el.move(initial_pos)
            else:
                # handles elements that arent a defined type.
                raise ValueError(f"Unsupported element type: {el_type}")

            self.elements[name] = el

    def _calculate_initial_position(self, data):
        """Calculated the initial position of each element based on data in
        json file."""

        # grab the offset of the given element
        ox, oy = data.get("offset", [0,0])

        if "align_to" in data:
            # aligns to an element if align_to is defined
            ref_name = data["align_to"]["name"]
            position = data["align_to"]["position"]
            ref_rect = self.elements[ref_name].rect
            if position == "bottom":
                return (ref_rect.left + ox, ref_rect.bottom + oy)
            elif position == "top":
                return (ref_rect.left + ox, ref_rect.top - data.get("size",[0,0])[1] + oy)
            elif position == "left":
                return (ref_rect.left - data.get("size",[0,0])[0] + ox, ref_rect.top + oy)
            elif position == "right":
                return (ref_rect.right + ox, ref_rect.top + oy)
                    
        elif "align" in data:
            # aligns to the screen if align is defined
            screen_rect = self.screen.get_rect()
            if data["align"] == "top_left":
                return (ox, oy)
            elif data["align"] == "top_right":
                return (screen_rect.width - data.get("size",[0,0])[0] - ox, oy)
            elif data["align"] == "bottom_left":
                return (ox, screen_rect.height - data.get("size",[0,0])[1] - oy)
            elif data["align"] == "bottom_right":
                return (screen_rect.width - data.get("size",[0,0])[0] - ox,
                        screen_rect.height - data.get("size",[0,0])[1] - oy)
            elif data["align"] == "center":
                return (screen_rect.centerx - data.get("size",[0,0])[0]//2,
                        screen_rect.centery - data.get("size",[0,0])[1]//2)
        return None
            # align at (0,0) if neither are defined.  

    def _place_container_children(self):
        """Place children in thier respective containers."""

        for cname, container in self.containers.items():
            crect = container["rect"]
            children = [self.elements[ch] for ch in container["children"] if ch in self.elements]
            layout = container.get("layout", {})
            spacing = layout.get("spacing", 10)
            direction = layout.get("type", "vertical")

            if direction == "vertical":
                # place children vertically in the container.
                # defaults to left center
                align_children = layout.get("align_children", "left")
                vertical_align = layout.get("vertical_align", "center")
                self.container_layout.place_vertical(
                    crect, children, spacing=spacing, align=align_children, vertical_align=vertical_align
                )
                # place children vertically in the container.
                # defaults to top center
            elif direction == "horizontal":
                align_children = layout.get("align_children", "top")
                horizontal_align = layout.get("horizontal_align", "center")
                self.container_layout.place_horizontal(
                    crect, children, spacing=spacing, align=align_children, horizontal_align=horizontal_align
                )

    def _align_to_screen(self, rect, align_type, ox=0, oy=0):
        """Aligns elements to the screen given the align{type} value
        from the json file"""

        screen_rect = self.screen.get_rect()
        if align_type == "center":
            rect.center = screen_rect.center
        elif align_type == "top_center":
            rect.midtop = (screen_rect.centerx + ox, oy)
        elif align_type == "bottom_center":
            rect.midbottom = (screen_rect.centerx + ox, screen_rect.bottom - oy)
        elif align_type == "top_left":
            rect.topleft = (ox, oy)
        elif align_type == "top_right":
            rect.topright = (screen_rect.width - ox, oy)
        elif align_type == "bottom_left":
            rect.bottomleft = (ox, screen_rect.height - oy)
        elif align_type == "bottom_right":
            rect.bottomright = (screen_rect.width - ox, screen_rect.height - oy)


    def _align_to_element(self, el, ref_rect, position, offset):
        """Aligns an element to another element given the 
        align_to{name, position} values in json"""

        ox, oy = offset
        if position == "bottom":
            el.rect.midtop = (ref_rect.midbottom[0] + ox, ref_rect.bottom + oy)
        elif position == "top":
            el.rect.midbottom = (ref_rect.midtop[0] + ox, ref_rect.top + oy)
        elif position == "left":
            el.rect.midright = (ref_rect.left + ox, ref_rect.centery + oy)
        elif position == "right":
            el.rect.midleft = (ref_rect.right + ox, ref_rect.centery + oy)
