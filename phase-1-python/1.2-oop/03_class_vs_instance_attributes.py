class Cars:
    # you can use something called "class attribute" when all object have something in common
    # It makes you saves trouble of saving the same attribute again and again
    # this saves tons of memory because when you have objects in large amount
    thing_type = "Car"
    model = "Anonymous"

    # instance attribue > class attributes
    def __init__(self, model, colour, model_no):
        self.model = model
        self.colour = colour
        self.model_no = model_no


car_1 = Cars("Lambo", "blue", "8y8")
car_2 = Cars("Toyota", "black", "34I2")
car_3 = Cars(Cars.model, "white", "YtY2")
print(car_1.model, car_1.colour, car_1.model_no, car_1.thing_type)
print(car_2.model, car_2.colour, car_2.model_no, car_2.thing_type)
print(car_3.model, car_3.colour, car_3.model_no, car_3.thing_type)
