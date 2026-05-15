import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def get_area(self):
        return math.pi * (self.radius**2)

    @property
    def get_perimeter(self):
        return (2 * self.radius) * math.pi


def main():
    radius = float(input("Enter the radius of a circle : "))
    c1 = Circle(radius)

    area_or_perimeter = int(
        input(
            "If you want to get area of circle then enter 1 and if you want perimeter press 2 : "
        )
    )

    if area_or_perimeter == 1:
        print(f"the area of circle is = {c1.get_area}")
    elif area_or_perimeter == 2:
        print(f"the perimeter of circle is = {c1.get_perimeter}")
    else:
        print("Invalid input please try again !")


if __name__ == "__main__":
    main()
