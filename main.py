class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


def get_count_of_small_rectangles_in_big_rectangle(big_rectangle: Rectangle, small_rectangle: Rectangle) -> int:
    width = big_rectangle.width // small_rectangle.width
    height = big_rectangle.height // small_rectangle.height
    return width * height


def get_max_count_of_small_rectangles_in_big_rectangle(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    roof_rectangle = Rectangle(roof_width, roof_height)
    panel_rectangle = Rectangle(panel_width, panel_height)
    panel_rectangle_rotate = Rectangle(panel_height, panel_width)
    count = get_count_of_small_rectangles_in_big_rectangle(
        roof_rectangle, panel_rectangle)
    count_rotate = get_count_of_small_rectangles_in_big_rectangle(
        roof_rectangle, panel_rectangle_rotate)

    max_count = max(count, count_rotate)
    print(f'Cantidad de rectángulos horizontales: {count}')
    print(f'Cantidad de rectángulos verticales: {count_rotate}')
    print(f'Máxima cantidad de rectángulos: {max_count}')


def main():
    get_max_count_of_small_rectangles_in_big_rectangle(1, 2, 2, 4)
    get_max_count_of_small_rectangles_in_big_rectangle(1, 2, 3, 5)
    get_max_count_of_small_rectangles_in_big_rectangle(2, 2, 1, 10)


if __name__ == "__main__":
    main()
