# container_layout.py

class ContainerLayout:
    """Handles arranging children inside a container.
    Supports vertical and horizontal layouts with spacing and alignment."""

    def place_vertical(self, container_rect, children, spacing=10, align="left", vertical_align="center"):
        """Handles arranging container children in a vertical alignment."""
        total_height = sum(child.rect.height for child in children) + spacing * (len(children)-1)

        # Determine starting y based on vertical alignment
        if vertical_align == "top":
            y = container_rect.top
        elif vertical_align == "center":
            y = container_rect.top + (container_rect.height - total_height)//2
        elif vertical_align == "bottom":
            y = container_rect.bottom - total_height
        else:
            y = container_rect.top

        for child in children:
            # Determine x based on horizontal alignment
            if align == "left":
                x = container_rect.left + child.offset[0]
            elif align == "center":
                x = container_rect.centerx - child.rect.width // 2 + child.offset[0]
            elif align == "right":
                x = container_rect.right - child.rect.width + child.offset[0]
            else:
                x = container_rect.left + child.offset[0]

            # Move element using its own move() method
            child.move((x, y + child.offset[1]))

            # Increment y for next child
            y += child.rect.height + spacing

    def place_horizontal(self, container_rect, children, spacing=10, align="top", horizontal_align="center"):
        """Handles arranging container children in horizontal alignment"""
        total_width = sum(child.rect.width for child in children) + spacing * (len(children)-1)

        # Determine starting x based on horizontal alignment
        if horizontal_align == "left":
            x = container_rect.left
        elif horizontal_align == "center":
            x = container_rect.left + (container_rect.width - total_width)//2
        elif horizontal_align == "right":
            x = container_rect.right - total_width
        else:
            x = container_rect.left

        for child in children:
            # Determine y based on vertical alignment
            if align == "top":
                y = container_rect.top + child.offset[1]
            elif align == "center":
                y = container_rect.centery - child.rect.height // 2 + child.offset[1]
            elif align == "bottom":
                y = container_rect.bottom - child.rect.height + child.offset[1]
            else:
                y = container_rect.top + child.offset[1]

            # Move element using its own move() method
            child.move((x + child.offset[0], y))

            # Increment x for next child
            x += child.rect.width + spacing
