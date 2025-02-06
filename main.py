class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

    def can_fit(self, other: "Rectangle") -> bool:
        return (self.width >= other.width and self.height >= other.height) or (
            self.width >= other.height and self.height >= other.width
        )


class TriangleIsosceles:
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    def get_largest_inscribed_rectangle(self) -> Rectangle:
        rect_width = self.base / 2
        rect_height = self.height / 2
        return Rectangle(int(rect_width), int(rect_height))


def count_fit_panels(roof: Rectangle, panel: Rectangle) -> int:
    return (roof.width // panel.width) * (roof.height // panel.height)


def evaluate_remaining_space(used_width: int, used_height: int, roof: Rectangle, panel: Rectangle, rotated_panel: Rectangle) -> int:
    remaining_sections = [
        Rectangle(roof.width - used_width, roof.height),
        Rectangle(roof.width, roof.height - used_height)
    ]

    return max(
        (count_fit_panels(section, rotated_panel) if section.can_fit(rotated_panel) else 0) +
        (count_fit_panels(section, panel) if section.can_fit(panel) else 0)
        for section in remaining_sections
    )


def maximize_panel_placement(roof: Rectangle, panel: Rectangle) -> int:
    if not roof.can_fit(panel):
        return 0

    rotated_panel = Rectangle(panel.height, panel.width)

    count_original = count_fit_panels(roof, panel)
    count_rotated = count_fit_panels(roof, rotated_panel)
    max_count = max(count_original, count_rotated)

    used_width_original = (roof.width // panel.width) * panel.width
    used_height_original = (roof.height // panel.height) * panel.height

    used_width_rotated = (
        roof.width // rotated_panel.width) * rotated_panel.width
    used_height_rotated = (
        roof.height // rotated_panel.height) * rotated_panel.height

    max_original = count_original + evaluate_remaining_space(
        used_width_original, used_height_original, roof, panel, rotated_panel)
    max_rotated = count_rotated + evaluate_remaining_space(
        used_width_rotated, used_height_rotated, roof, panel, rotated_panel)

    return max(max_count, max_original, max_rotated)


def max_panels_in_roof(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> None:
    roof_rectangle = Rectangle(roof_width, roof_height)
    panel_rectangle = Rectangle(panel_width, panel_height)
    max_combination = maximize_panel_placement(roof_rectangle, panel_rectangle)
    print(f'Máxima combinación: {max_combination}\n')
    return max_combination


def max_panels_in_triangle(base_triangle: int, height_triangle: int, panel_width: int, panel_height: int) -> None:
    triangle = TriangleIsosceles(base_triangle, height_triangle)
    largest_rectangle = triangle.get_largest_inscribed_rectangle()
    print(f'Máxima combinación en el triángulo:')
    return max_panels_in_roof(panel_width, panel_height,
                              largest_rectangle.width, largest_rectangle.height)


def main():
    max_panels_in_roof(1, 2, 2, 4)
    max_panels_in_roof(1, 2, 3, 5)
    max_panels_in_roof(2, 2, 1, 10)
    max_panels_in_roof(2, 3, 5, 5)
    max_panels_in_roof(3, 3, 2, 2)
    max_panels_in_roof(2, 3, 3, 4)

    max_panels_in_triangle(10, 6, 2, 2)
    max_panels_in_triangle(10, 10, 2, 3)


if __name__ == "__main__":
    main()
