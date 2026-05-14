class Animal:
    @staticmethod
    def __eats():
        return "Eats"

    def get_eating(self):
        return self.__eats()

    @staticmethod
    def __sleeps():
        return "Sleeps"

    def get_sleeping(self):
        return self.__sleeps()


class Dog(Animal):
    def bark(self):
        print("The dog barks !")

    def eat(self):
        print(f"The dog {self.get_eating()}")

    def sleep(self):
        print(f"The dog {self.get_sleeping()}")


class Cat(Animal):
    def meow(self):

        print("The Cat meows !")

    def eat(self):
        print(f"The cat {self.get_eating()}")

    def sleep(self):
        print(f"The cat {self.get_sleeping()}")


cat1 = Cat()
dog1 = Dog()

cat1.eat()
dog1.sleep()
