class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


def count_fit_panels(roof: Rectangle, panel: Rectangle) -> int:
    return (roof.width // panel.width) * (roof.height // panel.height)


def maximize_panel_placement(roof: Rectangle, panel: Rectangle) -> int:
    if roof.width < panel.width or roof.height < panel.height:
        return 0

    rotated_panel = Rectangle(panel.height, panel.width)
    max_count = count_fit_panels(roof, panel)

    used_width = (roof.width // panel.width) * panel.width
    used_height = (roof.height // panel.height) * panel.height

    if used_height == roof.height and used_width == roof.width:
        return max_count

    remaining_width = roof.width - used_width
    remaining_height = roof.height - used_height
    remaining_sections = []

    if remaining_width > 0:
        remaining_sections.append(Rectangle(remaining_width, roof.height))

    if remaining_height > 0:
        remaining_sections.append(Rectangle(roof.width, remaining_height))

    max_count += sum(count_fit_panels(section, rotated_panel)
                     for section in remaining_sections)

    return max_count


def max_panels_in_roof(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    roof_rectangle = Rectangle(roof_width, roof_height)
    panel_rectangle = Rectangle(panel_width, panel_height)
    max_combination = maximize_panel_placement(roof_rectangle, panel_rectangle)
    print(f'Máxima combinación: {max_combination}\n')


def main():
    max_panels_in_roof(1, 2, 2, 4)
    max_panels_in_roof(1, 2, 3, 5)
    max_panels_in_roof(2, 2, 1, 10)


if __name__ == "__main__":
    main()
