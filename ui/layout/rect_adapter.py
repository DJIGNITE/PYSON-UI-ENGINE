# rect_adapter.py

class RectAdapter:
    """Allows vertical/horizontal layout code to be unified."""

    __slots__ = ("r", "axis")

    def __init__(self, rect, axis: str):
        """Set the primary axis as x or y"""
        if axis not in ("x", "y"):
            raise ValueError("RectAdapter axis must be 'x' or 'y'")
        self.r = rect
        self.axis = axis

    @property
    def start(self) -> int:
        """Sets the start as left or top depending on the primary axis."""
        return self.r.left if self.axis == "x" else self.r.top

    @start.setter
    def start(self, val: int):
        """Works with above start property to set the start value."""
        if self.axis == "x":
            self.r.left = val
        else:
            self.r.top = val

    @property
    def end(self) -> int:
        """Sets the end as either right or bottom depending on primary axis."""
        return self.r.right if self.axis == "x" else self.r.bottom

    @end.setter
    def end(self, val: int):
        """Works with end property to set the end value."""
        if self.axis == "x":
            self.r.right = val
        else:
            self.r.bottom = val

    @property
    def center(self) -> int:
        """Sets the center as centerx or centery depending on the element's
        primary axis"""
        return self.r.centerx if self.axis == "x" else self.r.centery

    @center.setter
    def center(self, val: int):
        """Works with the center property to set the center value"""
        if self.axis == "x":
            self.r.centerx = val
        else:
            self.r.centery = val

    @property
    def size(self) -> int:
        """Sets the size value as the width or height depending on the 
        axis."""
        return self.r.width if self.axis == "x" else self.r.height

    @size.setter
    def size(self, val: int):
        """Works with the size property to set the size."""
        if val < 0:
            # make certain that this property is not 0
            raise ValueError("Size must be non-negative")
        if self.axis == "x":
            self.r.width = val
        else:
            self.r.height = val

    def advance(self, amount: int):
        """Move the element forward along the primary axis."""
        self.start += amount

    def stretch_to(self, container_adapter, padding=0):
        """Stretch this element to match container size on this axis."""
        self.start = container_adapter.start + padding
        self.end = container_adapter.end - padding

    def __repr__(self):
        """Set representation for debugging."""
        return f"RectAdapter(axis={self.axis}, rect={self.r})"
