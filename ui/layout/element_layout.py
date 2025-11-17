# element_layout.py

class ElementLayout:
    """Class to handle element alignment relative to other elements."""

    def apply_align_to(self, elements):
        """Use align_to if the property if it is found for an element in the
        json file. Align elements to each other."""
        for name, element in elements.items():
            # check for align_to
            if hasattr(element, "align_to") and element.align_to:
                ref_name = element.align_to["name"]
                position = element.align_to["position"]
                if ref_name not in elements:
                    continue
                ref_rect = elements[ref_name].rect
                offset_x, offset_y = element.offset

                # position element to it's reference element.
                if position == "bottom":
                    element.rect.midtop = (ref_rect.midbottom[0] + offset_x, ref_rect.bottom + offset_y)
                elif position == "top":
                    element.rect.midbottom = (ref_rect.midtop[0] + offset_x, ref_rect.top + offset_y)
                elif position == "left":
                    element.rect.midright = (ref_rect.left + offset_x, ref_rect.centery + offset_y)
                elif position == "right":
                    element.rect.midleft = (ref_rect.right + offset_x, ref_rect.centery + offset_y)
