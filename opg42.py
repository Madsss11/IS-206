## is-a
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Cat(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Person(object):

    def __init__(self, name):
        ## has-a
        self.name = name

        ## has-a
        self.pet = None

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## is-a
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## has-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


## is-a
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

## is-a
mary = Person("Mary")

## has-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()