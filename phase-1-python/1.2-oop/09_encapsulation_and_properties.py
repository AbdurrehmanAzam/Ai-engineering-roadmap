# Private attributes are used for Accessing the attribute only within the class
# Objects cant use private attributes
# Placing __ before attribute can make that attribute private
class Patient:
    def __init__(self, name, phone_number, id):
        self.name = name
        self.__phone_number = phone_number
        self.__id = id

    @property
    def phone_number(self):
        return self.__phone_number

    def get_personal_data(self):
        return print(
            f"This person ID is = {self.__id}\nphone number is = {self.phone_number}"
        )


# Since phone number is sensitive data you need to make user unable to access  it
# but you can use this private attribute with class
p1 = Patient("Abdurrehman", "0928*******", "1")
p1.get_personal_data()
